from flask import Flask, request, jsonify, render_template
import mmh3
from bitarray import bitarray

app = Flask(__name__)

class BloomFilter:
    def __init__(self, size=100, hash_count=7):
        """Initialize a Bloom filter with specified size and 7 hash functions."""
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        """Generate 7 hash positions for an item using MurmurHash3."""
        return [mmh3.hash(item, seed=i) % self.size for i in range(self.hash_count)]

    def add(self, item):
        """Add an item (e.g., profile ID) to the Bloom filter."""
        indices = self._hashes(item)
        for index in indices:
            self.bit_array[index] = 1
        return indices, list(self.bit_array)

    def check(self, item):
        """Check if an item might be in the filter or is definitely not."""
        indices = self._hashes(item)
        for index in indices:
            if not self.bit_array[index]:
                return indices, list(self.bit_array), "Not in the list—show it!"
        return indices, list(self.bit_array), "Might be in the list—skip it!"

# Global Bloom filter instance
bloom_filter = BloomFilter(size=100, hash_count=7)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/status')
def status():
    """Return the current bit array state."""
    return jsonify({'bit_array': list(bloom_filter.bit_array)})

@app.route('/add', methods=['POST'])
def add_item():
    """Add a profile ID to the Bloom filter."""
    data = request.get_json()
    item = data.get('item')
    if not item:
        return jsonify({'error': 'No profile ID provided'}), 400
    indices, bit_array = bloom_filter.add(item)
    return jsonify({'indices': indices, 'bit_array': bit_array, 'message': f'Added {item}'})

@app.route('/check', methods=['POST'])
def check_item():
    """Check if a profile ID is in the Bloom filter."""
    data = request.get_json()
    item = data.get('item')
    if not item:
        return jsonify({'error': 'No profile ID provided'}), 400
    indices, bit_array, result = bloom_filter.check(item)
    return jsonify({'indices': indices, 'bit_array': bit_array, 'result': result})

if __name__ == '__main__':
    # Preload 10 items to increase false positive probability
    for i in range(10):
        bloom_filter.add(f'preload{i}')
    app.run(debug=True)