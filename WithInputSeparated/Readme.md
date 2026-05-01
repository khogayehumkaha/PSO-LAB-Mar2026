
# 📘 PSO Lab – Complete Solutions 
---

# 🔹 PART – A

---

## 1. #303 Range Sum Query (Prefix Sum)

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)


Given an integer array `nums`, handle multiple queries to calculate the sum of elements between indices `left` and `right` (inclusive).

---

### 💻 Code

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]
```

---

### ▶️ Execution

```python
# Input
nums = [1,2,3,4]
obj = NumArray(nums)

# Output
print(obj.sumRange(1,3))
```

---

### ✅ Output

```
9
```

---

### 💡 Explanation

This problem is solved using the **Prefix Sum technique**, which helps avoid recalculating sums for every query.

Step 1: Build Prefix Array
For `nums = [1,2,3,4]`, we create:

```
prefix = [0, 1, 3, 6, 10]
```

Each index stores the cumulative sum up to that point.

---

Step 2: Use Formula

```
sumRange(left, right) = prefix[right+1] - prefix[left]
```

For `left = 1`, `right = 3`:

```
prefix[4] = 10   (sum of all elements)
prefix[1] = 1    (sum before index 1)

Result = 10 - 1 = 9
```

---

### 🎯 Key Idea

👉 Instead of computing `2 + 3 + 4` every time, we subtract the unwanted left portion.

---

### 🚀 Complexity

* Time per query: **O(1)**
* Preprocessing time: **O(n)**


---


## 2. #560 Subarray Sum Equals K

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find the total number of continuous subarrays whose sum equals `k`.

---

### 💻 Code

```python id="u9s8a1"
def subarraySum(nums, k):
    d = {0:1}
    total = 0
    count = 0

    for n in nums:
        total += n
        if total - k in d:
            count += d[total - k]
        d[total] = d.get(total, 0) + 1

    return count
```

---

### ▶️ Execution

```python id="7f3k2p"
# Input
nums = [1,1,1]
k = 2

# Output
print(subarraySum(nums, k))
```

---

### ✅ Output

```id="2h8x0q"
2
```

---

### 💡 Explanation

This problem is solved using the **Prefix Sum + HashMap technique**, which helps efficiently count subarrays without checking all possibilities.

---

### 🔹 Step 1: Initialize

```id="l2k9zn"
d = {0:1}
```

👉 This means sum `0` has occurred once (helps when subarray starts from index 0)

---

### 🔹 Step 2: Traverse Array

We maintain:

* `total` → cumulative sum
* `d` → stores frequency of prefix sums

---

### 🔹 Step-by-step for nums = [1,1,1], k = 2

```id="5k1qnv"
Index 0 → total = 1 → no match
Index 1 → total = 2 → (2-2=0 found) → count = 1
Index 2 → total = 3 → (3-2=1 found) → count = 2
```

---

### 🎯 Key Idea

```id="n3p9bd"
If (current_sum - k) exists in map → valid subarray found
```

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(n)**


---

## 3. #125 Valid Palindrome

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Check whether a string is a palindrome after removing non-alphanumeric characters and ignoring case.

---

### 💻 Code

```python id="c1p8zk"
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

---

### ▶️ Execution

```python id="8m2qxr"
# Input
s = "A man, a plan, a canal: Panama"

# Output
print(isPalindrome(s))
```

---

### ✅ Output

```id="v7k1zd"
True
```

---

### 💡 Explanation

This problem is solved in **two steps: cleaning + comparison**.

---

### 🔹 Step 1: Clean the String

Remove non-alphanumeric characters and convert to lowercase:

```id="q3n5yt"
"A man, a plan, a canal: Panama"
→ "amanaplanacanalpanama"
```

---

### 🔹 Step 2: Compare with Reverse

```id="p9x2fw"
s == s[::-1]
```

👉 This checks if the string reads the same forward and backward.

---

### 🎯 Key Idea

👉 A string is a palindrome if:

```id="m8t6gh"
original == reversed
```

---

### 🧠 Note

Even though slicing is used, logically it works like **Two Pointers**:

* One pointer from start
* One pointer from end
* Compare characters moving inward

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(n)**


---

## 4. #167 Two Sum II

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find two numbers in a sorted array that add up to a target.

---

### 💻 Code

```python id="t2p7xk"
def twoSum(numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
```

---

### ▶️ Execution

```python id="6kq9mz"
# Input
numbers = [2,7,11,15]
target = 9

# Output
print(twoSum(numbers, target))
```

---

### ✅ Output

```id="y3v8pd"
[1, 2]
```

---

### 💡 Explanation

This problem is solved using the **Two Pointers technique**, which works efficiently on a **sorted array**.

---

### 🔹 Step 1: Initialize Pointers

```id="n8r2qw"
l = 0 (start)
r = 3 (end)
```

---

### 🔹 Step-by-step Execution

```id="4f7kzx"
Step 1: 2 + 15 = 17 → too large → move right pointer
Step 2: 2 + 11 = 13 → too large → move right pointer
Step 3: 2 + 7 = 9 → match found ✅
```

---

### 🔹 Return Result

```id="m5z1xt"
[l+1, r+1] → [1, 2]
```

👉 Indices are **1-based** as required.

---

### 🎯 Key Idea

```id="q2w6bn"
If sum < target → move left pointer
If sum > target → move right pointer
```

---

### 🧠 Why It Works

Since the array is sorted:

* Moving left pointer increases sum
* Moving right pointer decreases sum

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**



---

## 5. #643 Maximum Average Subarray

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find the maximum average of a subarray of length `k`.

---

### 💻 Code

```python id="x9k2bz"
def findMaxAverage(nums, k):
    window = sum(nums[:k])
    max_sum = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        max_sum = max(max_sum, window)

    return max_sum / k
```

---

### ▶️ Execution

```python id="3n7qvt"
# Input
nums = [1,12,-5,-6,50,3]
k = 4

# Output
print(findMaxAverage(nums, k))
```

---

### ✅ Output

```id="p4v8md"
12.75
```

---

### 💡 Explanation

This problem is solved using the **Sliding Window technique**, which avoids recalculating sums for every subarray.

---

### 🔹 Step 1: Initial Window

Take first `k` elements:

```id="a1s6df"
1 + 12 + (-5) + (-6) = 2
```

```id="z7x3kl"
window = 2
max_sum = 2
```

---

### 🔹 Step 2: Slide the Window

Instead of recomputing sum:

👉 **Add next element and remove previous element**

---

```id="q8m2yt"
Move 1 step:
Remove 1, Add 50 → window = 2 - 1 + 50 = 51
max_sum = 51
```

---

```id="n5r9bc"
Move next:
Remove 12, Add 3 → window = 51 - 12 + 3 = 42
max_sum = 51 (unchanged)
```

---

### 📊 Final Calculation

```id="k2t7zp"
max_sum = 51
average = 51 / 4 = 12.75
```

---

### 🎯 Key Idea

```id="w6x1op"
New Window = Previous Window + next element − outgoing element
```

---

### 🧠 Why It Works

Instead of recalculating every subarray (**O(n*k)**), we update in constant time → **O(n)**

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**


---

## 6. #3 Longest Substring Without Repeating

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find the length of the longest substring without repeating characters.

---

### 💻 Code

```python id="m2q9xk"
def lengthOfLongestSubstring(s):
    char_set = set()
    l = 0
    max_len = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_len = max(max_len, r-l+1)

    return max_len
```

---

### ▶️ Execution

```python id="8t5zvn"
# Input
s = "abcabcbb"

# Output
print(lengthOfLongestSubstring(s))
```

---

### ✅ Output

```id="p7r4dk"
3
```

---

### 💡 Explanation

This problem is solved using the **Sliding Window technique**, ensuring all characters in the window are unique.

---

### 🔹 Step 1: Initialize

We use:

* `l` → left pointer
* `r` → right pointer
* `char_set` → stores unique characters

---

### 🔹 Step-by-step Execution

```id="v3k1qb"
Start → ""

Add 'a' → "a" → length = 1  
Add 'b' → "ab" → length = 2  
Add 'c' → "abc" → length = 3 ✅
```

---

### 🔹 Handle Duplicate

Next character = `'a'` (duplicate)

```id="k9m2yt"
Remove 'a' from left → window = "bc"
Add 'a' → window = "bca"
```

---

### 🔹 Continue Process

```id="q4n8zs"
"cab" → length = 3  
"abc" → length = 3  
```

If duplicate appears:
👉 Keep removing from left until valid

---

### 🎯 Key Idea

```id="x7p3ld"
Expand window → if duplicate found, shrink from left
```

---

### 🧠 Why It Works

Each character is:

* Added once
* Removed once

👉 So total operations are linear

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(n)**


---

## 7. #141 Linked List Cycle

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Detect if a linked list contains a cycle.

---

### 💻 Code

```python id="p3k9zt"
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

### ▶️ Execution

```python id="8r2mvn"
# Input
head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node2.next = head   # cycle created

# Output
print(hasCycle(head))
```

---

### ✅ Output

```id="t6x1qd"
True
```

---

### 💡 Explanation

This problem is solved using the **Fast & Slow Pointer technique (Floyd’s Cycle Detection Algorithm)**.

---

### 🔹 Step 1: Initialize Pointers

```id="y4k8zs"
slow → moves 1 step  
fast → moves 2 steps
```

---

### 🔹 Structure of Linked List

```id="m9q2bt"
1 → 2
↑   ↓
← ← ←
```

👉 Node `2` points back to `1` → cycle exists

---

### 🔹 Step-by-step Execution

```id="z2p7wk"
Start:
slow = 1, fast = 1

Move:
slow → 2
fast → 1  (jumps 2 steps due to cycle)
```

👉 Both pointers meet → cycle detected ✅

---

### 🎯 Key Idea

```id="x5r3ld"
If fast pointer meets slow pointer → cycle exists
```

---

### 🧠 Why It Works

* Fast pointer moves faster
* In a cycle, it will eventually "lap" the slow pointer

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**


---

## 8. #876 Middle of Linked List

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Return the middle node of a linked list.

---

### 💻 Code

```python id="k4p9zt"
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val
```

---

### ▶️ Execution

```python id="9x2mvn"
# Input
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Output
print(middleNode(head))
```

---

### ✅ Output

```id="t8x1qd"
3
```

---

### 💡 Explanation

This problem is solved using the **Fast & Slow Pointer technique**.

---

### 🔹 Step 1: Initialize Pointers

```id="y2k8zs"
slow → moves 1 step  
fast → moves 2 steps
```

---

### 🔹 Linked List

```id="m3q2bt"
1 → 2 → 3 → 4
```

---

### 🔹 Step-by-step Execution

```id="z4p7wk"
Start:
slow = 1, fast = 1

Move:
slow → 2
fast → 3

Move again:
slow → 3
fast → None (end reached)
```

👉 Loop stops → slow is at middle node

---

### 🎯 Key Idea

```id="x2r3ld"
Fast moves 2 steps, slow moves 1 → slow reaches middle
```

---

### 🧠 Why It Works

* Fast pointer reaches end faster
* Slow pointer naturally lands at midpoint

👉 For even length, it returns the **second middle node**

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**


---

## 9. #206 Reverse Linked List

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Reverse a singly linked list.

---

### 💻 Code

```python id="r2k9zt"
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

### ▶️ Execution

```python id="6x2mvn"
# Input
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Output
rev = reverseList(head)
while rev:
    print(rev.val, end=" ")
    rev = rev.next
```

---

### ✅ Output

```id="t9x1qd"
3 2 1
```

---

### 💡 Explanation

This problem is solved using **in-place pointer reversal**.

---

### 🔹 Step 1: Initialize Pointers

```id="y6k8zs"
prev = None  
curr = head
```

---

### 🔹 Original List

```id="m1q2bt"
1 → 2 → 3 → None
```

---

### 🔹 Step-by-step Execution

```id="z7p7wk"
Step 1:
curr = 1 → reverse → 1 → None

Step 2:
curr = 2 → reverse → 2 → 1 → None

Step 3:
curr = 3 → reverse → 3 → 2 → 1 → None
```

---

### 🔹 Final Result

```id="x9r3ld"
3 → 2 → 1 → None
```

---

### 🎯 Key Idea

```id="p4w8gh"
Reverse each node’s next pointer to point to previous node
```

---

### 🧠 Why It Works

* We store next node (`nxt`) before breaking link
* Then reverse direction step by step

👉 List direction gets flipped completely

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**


---

## 10. #92 Reverse Linked List II

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Reverse nodes between positions `left` and `right`.

---

### 💻 Code

```python id="b7k2zt"
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left-1):
        prev = prev.next

    curr = prev.next
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
```

---

### ▶️ Execution

```python id="5x9mvn"
# Input
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Output
res = reverseBetween(head, 2, 3)
while res:
    print(res.val, end=" ")
    res = res.next
```

---

### ✅ Output

```id="n4x1qd"
1 3 2 4
```

---

### 💡 Explanation

This problem reverses **only a portion of the linked list** using **in-place pointer manipulation**.

---

### 🔹 Step 1: Use Dummy Node

```id="u2k8zs"
dummy → 0 → 1 → 2 → 3 → 4
```

👉 Helps handle edge cases easily

---

### 🔹 Step 2: Move `prev` to Node Before Reversal

For `left = 2`:

```id="m8q2bt"
prev → 1
```

---

### 🔹 Step 3: Reverse Sublist

Original:

```id="z1p7wk"
1 → 2 → 3 → 4
      ↑   ↑
    left right
```

---

### 🔁 Step-by-step

```id="x3r9ld"
Take node 3 and move it before node 2

1 → 3 → 2 → 4
```

👉 Only one iteration needed (`right - left = 1`)

---

### 🔹 Final Result

```id="p7w8gh"
1 → 3 → 2 → 4
```

---

### 🎯 Key Idea

```id="k2n6qp"
Pick next node and insert it at the front of the sublist
```

---

### 🧠 Why It Works

* We don't reverse entire list
* Only rearrange pointers within given range

👉 Efficient in-place transformation

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**



---

## 11. #496 Next Greater Element I

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find next greater element for each element in `nums1`.

---

### 💻 Code

```python id="h4k2zt"
def nextGreaterElement(nums1, nums2):
    stack = []
    d = {}

    for n in nums2:
        while stack and stack[-1] < n:
            d[stack.pop()] = n
        stack.append(n)

    return [d.get(x, -1) for x in nums1]
```

---

### ▶️ Execution

```python id="7x2mvn"
# Input
nums1 = [4,1,2]
nums2 = [1,3,4,2]

# Output
print(nextGreaterElement(nums1, nums2))
```

---

### ✅ Output

```id="t1x1qd"
[-1, 3, -1]
```

---

### 💡 Explanation

This problem is solved using a **Monotonic Stack**, which helps efficiently find the next greater element.

---

### 🔹 Step 1: Initialize

```id="y9k8zs"
stack = []     # decreasing stack
d = {}         # mapping of next greater elements
```

---

### 🔹 Step 2: Process nums2

```id="m4q2bt"
nums2 = [1,3,4,2]
```

---

### 🔁 Step-by-step

```id="z8p7wk"
Take 1 → push → stack = [1]

Take 3 → 3 > 1 → pop 1 → d[1] = 3
stack = [3]

Take 4 → 4 > 3 → pop 3 → d[3] = 4
stack = [4]

Take 2 → 2 < 4 → push → stack = [4,2]
```

---

### 🔹 Mapping Created

```id="x6r3ld"
d = {1:3, 3:4}
```

👉 Elements without greater value remain unmapped

---

### 🔹 Build Result for nums1

```id="p3w8gh"
nums1 = [4,1,2]

4 → -1  
1 → 3  
2 → -1
```

---

### 🎯 Key Idea

```id="k8n6qp"
Use stack to track decreasing elements → resolve when larger number appears
```

---

### 🧠 Why It Works

* Stack keeps elements waiting for next greater
* When bigger element appears → resolve all smaller ones

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## 12. #739 Daily Temperatures

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find number of days until a warmer temperature.

---

### 💻 Code

```python id="d2k9zt"
def dailyTemperatures(T):
    stack = []
    res = [0]*len(T)

    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)

    return res
```

---

### ▶️ Execution

```python id="8x2mvn"
# Input
T = [73,74,75,71,69,72,76,73]

# Output
print(dailyTemperatures(T))
```

---

### ✅ Output

```id="t2x1qd"
[1,1,4,2,1,1,0,0]
```

---

### 💡 Explanation

This problem is solved using a **Monotonic Stack**, which helps track the next warmer day efficiently.

---

### 🔹 Step 1: Initialize

```id="y7k8zs"
stack = []        # stores indices
res = [0,...,0]   # result array
```

---

### 🔹 Step 2: Process Temperatures

```id="m6q2bt"
T = [73,74,75,71,69,72,76,73]
```

---

### 🔁 Step-by-step

```id="z5p7wk"
Day 0 → 73 → push → stack = [0]

Day 1 → 74
→ 74 > 73 → res[0] = 1
stack = [1]

Day 2 → 75
→ 75 > 74 → res[1] = 1
stack = [2]

Day 3 → 71 → push
Day 4 → 69 → push
stack = [2,3,4]

Day 5 → 72
→ 72 > 69 → res[4] = 1
→ 72 > 71 → res[3] = 2

Day 6 → 76
→ resolves multiple:
res[5] = 1
res[2] = 4

Day 7 → 73 → no warmer → stays 0
```

---

### 🔹 Final Result

```id="x4r3ld"
[1,1,4,2,1,1,0,0]
```

---

### 🎯 Key Idea

```id="p6w8gh"
Store indices → when warmer day appears, calculate difference
```

---

### 🧠 Why It Works

* Stack keeps unresolved (colder) days
* When warmer day appears → resolve all smaller ones

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(n)**


---

# 🔹 PART – B 


---


## 1. #238 Product of Array Except Self

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Return array where each element is product of all elements except itself.

---

### 💻 Code

```python id="p8k2zt"
def productExceptSelf(nums):
    res = [1]*len(nums)

    left = 1
    for i in range(len(nums)):
        res[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res
```

---

### ▶️ Execution

```python id="7x4mvn"
# Input
nums = [1,2,3,4]

# Output
print(productExceptSelf(nums))
```

---

### ✅ Output

```id="t5x1qd"
[24, 12, 8, 6]
```

---

### 💡 Explanation

This problem is solved using the **Prefix (Left) + Suffix (Right) product technique**, without using division.

---

### 🔹 Step 1: Goal

```id="y3k8zs"
nums = [1,2,3,4]

Result:
[2×3×4, 1×3×4, 1×2×4, 1×2×3]
→ [24, 12, 8, 6]
```

---

### 🔹 Step 2: Left Product Pass

```id="m2q2bt"
res = [1,1,1,1]

Build left products:

res[0] = 1
res[1] = 1
res[2] = 2
res[3] = 6
```

👉 After left pass:

```id="z3p7wk"
res = [1,1,2,6]
```

---

### 🔹 Step 3: Right Product Pass

```id="x1r3ld"
Multiply with right products:

res[3] = 6 * 1 = 6
res[2] = 2 * 4 = 8
res[1] = 1 * 12 = 12
res[0] = 1 * 24 = 24
```

---

### 🔹 Final Result

```id="p9w8gh"
[24, 12, 8, 6]
```

---

### 🎯 Key Idea

```id="k5n6qp"
For each index → result = left product × right product
```

---

### 🧠 Why It Works

* First pass stores left-side products
* Second pass multiplies right-side products

👉 No division needed (handles zero safely)

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)** (excluding output array)


---

## 2. #11 Container With Most Water

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find max water container area.

---

### 💻 Code

```python id="c4k2zt"
def maxArea(height):
    l, r = 0, len(height)-1
    max_area = 0

    while l < r:
        h = min(height[l], height[r])
        max_area = max(max_area, h*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area
```

---

### ▶️ Execution

```python id="9x4mvn"
# Input
height = [1,8,6,2,5,4,8,3,7]

# Output
print(maxArea(height))
```

---

### ✅ Output

```id="t3x1qd"
49
```

---

### 💡 Explanation

This problem is solved using the **Two Pointers technique** to efficiently maximize area.

---

### 🔹 Step 1: Formula

```id="y5k8zs"
Area = min(height[left], height[right]) × (right - left)
```

---

### 🔹 Step 2: Initialize Pointers

```id="m7q2bt"
l = 0 (start)
r = n-1 (end)
```

---

### 🔁 Step-by-step

```id="z9p7wk"
Step 1:
l=0 (1), r=8 (7)
Area = min(1,7) × 8 = 8

Move left pointer (smaller height)
```

---

```id="x8r3ld"
Step 2:
l=1 (8), r=8 (7)
Area = min(8,7) × 7 = 49 ✅
```

---

### 🔹 Continue Process

👉 Always move the pointer with **smaller height**

```id="p1w8gh"
Reason:
Smaller height limits water capacity
```

---

### 🔹 Final Result

```id="k9n6qp"
Maximum Area = 49
```

---

### 🎯 Key Idea

```id="v6t2qs"
Move pointer with smaller height to try increasing area
```

---

### 🧠 Why It Works

* Width decreases each step
* We try to increase height strategically

👉 Avoids brute force O(n²)

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**




---

## 3. #424 Longest Repeating Character Replacement

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Find longest substring with same characters after at most `k` replacements.

---

### 💻 Code

```python id="r7k2zt"
def characterReplacement(s, k):
    count = {}
    l = 0
    maxf = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r-l+1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r-l+1)

    return res
```

---

### ▶️ Execution

```python id="6x4mvn"
# Input
s = "AABABBA"
k = 1

# Output
print(characterReplacement(s, k))
```

---

### ✅ Output

```id="t7x1qd"
4
```

---

### 💡 Explanation

This problem is solved using the **Sliding Window technique** to maintain a valid substring.

---

### 🔹 Step 1: Key Idea

```id="y1k8zs"
(window size) - (most frequent character count) ≤ k
```

👉 Means we can replace remaining characters to make all same

---

### 🔹 Step 2: Initialize

```id="m5q2bt"
l → left pointer  
r → right pointer  
count → frequency map  
maxf → max frequency in window
```

---

### 🔁 Step-by-step

```id="z6p7wk"
Start building window:

"AAB"
maxf = 2 → valid (3 - 2 ≤ 1)

"AABA"
maxf = 3 → valid (4 - 3 ≤ 1)

"AABAB"
window = 5, maxf = 3
5 - 3 = 2 > k → invalid ❌
```

---

### 🔹 Shrink Window

```id="x2r3ld"
Remove from left until valid again
```

---

### 🔹 Final Result

```id="p8w8gh"
Maximum valid substring length = 4
```

---

### 🎯 Key Idea

```id="k1n6qp"
Expand window → shrink when (window - maxf > k)
```

---

### 🧠 Why It Works

* Always keep window valid
* Track most frequent char to minimize replacements

👉 Efficiently avoids checking all substrings

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)** (since only 26 uppercase letters)



---

## 4. #19 Remove Nth Node From End

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Remove the `n`th node from the end of a linked list.

---

### 💻 Code

```python id="q2k9zt"
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
```

---

### ▶️ Execution

```python id="5x4mvn"
# Input
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
n = 2

# Output
res = removeNthFromEnd(head, n)
while res:
    print(res.val, end=" ")
    res = res.next
```

---

### ✅ Output

```id="t4x1qd"
1 3
```

---

### 💡 Explanation

This problem is solved using the **Fast & Slow Pointer technique** with a fixed gap.

---

### 🔹 Step 1: Use Dummy Node

```id="y8k8zs"
dummy → 0 → 1 → 2 → 3
```

👉 Helps handle edge cases (like removing head)

---

### 🔹 Step 2: Move Fast Pointer

```id="m3q2bt"
Move fast pointer n steps ahead

fast → 2 steps ahead of slow
```

---

### 🔹 Step 3: Move Both Pointers

```id="z2p7wk"
Move fast and slow together:

fast → reaches end  
slow → reaches node before target
```

---

### 🔹 Step 4: Remove Node

```id="x7r3ld"
slow.next = slow.next.next
```

👉 Skips the target node

---

### 🔹 Example

```id="p2w8gh"
Original: 1 → 2 → 3  
Remove 2nd from end → remove 2  

Result: 1 → 3
```

---

### 🎯 Key Idea

```id="k6n6qp"
Keep a gap of n between fast and slow → slow reaches node before deletion
```

---

### 🧠 Why It Works

* Fast reaches end first
* Slow automatically lands at correct position

👉 One pass solution

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**



---

## 5. #61 Rotate List

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Rotate linked list to the right by `k` positions.

---

### 💻 Code

```python id="u3k9zt"
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def rotateRight(head, k):
    if not head:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    tail.next = head
    steps = length - k
    new_tail = head

    for _ in range(steps-1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
```

---

### ▶️ Execution

```python id="4x4mvn"
# Input
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
k = 1

# Output
res = rotateRight(head, k)
while res:
    print(res.val, end=" ")
    res = res.next
```

---

### ✅ Output

```id="t9x2qd"
3 1 2
```

---

### 💡 Explanation

This problem is solved by converting the list into a **circular linked list**, then breaking it at the correct position.

---

### 🔹 Step 1: Find Length & Tail

```id="y2k8zs"
1 → 2 → 3

length = 3  
tail = 3
```

---

### 🔹 Step 2: Optimize k

```id="m9q2bt"
k = k % length = 1 % 3 = 1
```

👉 Avoid unnecessary full rotations

---

### 🔹 Step 3: Make Circular List

```id="z4p7wk"
tail.next = head

1 → 2 → 3
↑       ↓
← ← ← ← ←
```

---

### 🔹 Step 4: Find New Tail

```id="x5r3ld"
steps = length - k = 3 - 1 = 2

Move 2 steps → new_tail = 2
```

---

### 🔹 Step 5: Break the Circle

```id="p6w8gh"
new_head = 3  
new_tail.next = None
```

---

### 🔹 Final Result

```id="k3n6qp"
3 → 1 → 2
```

---

### 🎯 Key Idea

```id="v7t2qs"
Make list circular → break at correct position
```

---

### 🧠 Why It Works

* Rotating right = shifting break point
* Circular structure makes rotation easy

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**


---

## 6. #901 Online Stock Span

![Question](https://img.shields.io/badge/Question-Problem-blue?style=for-the-badge)

Calculate stock span for each day.

---

### 💻 Code

```python id="s2k9zt"
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```

---

### ▶️ Execution

```python id="6x4mvn"
# Input /  Output
sp = StockSpanner()

print(sp.next(100))
print(sp.next(80))
print(sp.next(60))
print(sp.next(70))
print(sp.next(60))
print(sp.next(75))
print(sp.next(85))
```

---

### ✅ Output

```id="t8x1qd"
1
1
1
2
1
4
6
```

---

### 💡 Explanation

This problem is solved using a **Monotonic Stack**, which efficiently calculates stock spans.

---

### 🔹 Step 1: Key Idea

```id="y4k8zs"
Stock Span = number of consecutive days where price ≤ today's price
```

---

### 🔹 Step 2: Stack Structure

```id="m6q2bt"
stack stores (price, span)
```

👉 Maintains **decreasing order of prices**

---

### 🔁 Step-by-step

```id="z3p7wk"
Price = 100 → push → span = 1
stack = [(100,1)]

Price = 80 → push → span = 1
stack = [(100,1),(80,1)]

Price = 60 → push → span = 1

Price = 70
→ 70 > 60 → pop → span = 1 + 1 = 2

Price = 60 → push → span = 1

Price = 75
→ pop 60, 70 → span = 4

Price = 85
→ pop 75, 80 → span = 6
```

---

### 🔹 Final Output

```id="x2r3ld"
1
1
1
2
1
4
6
```

---

### 🎯 Key Idea

```id="p5w8gh"
Pop all smaller prices and add their spans
```

---

### 🧠 Why It Works

* Combines previous spans instead of recalculating
* Each element processed only once

👉 Efficient merging using stack

---

### 🚀 Complexity

* Time: **O(n)**
* Space: **O(n)**

---
