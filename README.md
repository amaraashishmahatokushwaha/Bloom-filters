# **Bloom Filter: Dating App Left-Swipe Tracker**

This is a **Flask web application** that demonstrates a **Bloom filter** for tracking *left-swiped profiles* in a dating app. Users can add profile IDs (*simulating a left swipe*), check if a profile should be shown or skipped, and see an **animated bit array** showing how the filter works. The app also showcases a **false positive** case, where a profile *not added* might be flagged as *"skip"* due to overlapping bits.

The interface is **user-friendly**, with a **clean design**, **smooth animations**, and **clear feedback**. Built with **Python (Flask)** for the backend and **HTML/JavaScript/Tailwind CSS** for the frontend, it’s perfect for learning about **Bloom filters** in a *practical context*.

---

## **Features**

- **Add Profiles**: Simulate a *left swipe* by adding a profile ID to the Bloom filter.
- **Check Profiles**: See if a profile is *"Might be in the list—skip it!"* or *"Not in the list—show it!"*
- **Animated Bit Array**: Watch a 10x10 bit array animate as bits flip, with sequential highlights for hash positions.
- **False Positive Demo**: Test a profile (*fakeuser*) to see a possible *false positive*, with an explanation.
- **Responsive UI**: Works on desktop and mobile, with a **progress bar** and **color-coded results**.

---

## **Prerequisites**

- **Python 3.6 or higher**
- **Git** (for cloning the repository)
- A *web browser* (e.g., Chrome, Firefox)

---

## **Setup Instructions**

### **Clone the Repository**
```bash
git clone https://github.com/your-username/bloomfilter.git
cd bloomfilter
