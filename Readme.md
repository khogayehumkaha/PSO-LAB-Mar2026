
# 📘 PSO Lab – Complete Solutions 
---

# 🔹 PART – A

---

## 1. #303 Range Sum Query (Prefix Sum)

### ❓ Question

Given an integer array `nums`, handle multiple queries to calculate the sum of elements between indices `left` and `right` (inclusive).

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

### ▶️ Execution

```python
nums = [1,2,3,4]
obj = NumArray(nums)
print(obj.sumRange(1,3))
```

### ✅ Output

```
9
```

### 💡 Explanation

Prefix sum stores cumulative values, allowing O(1) range sum queries.

This code uses the Prefix Sum technique to answer range sum queries efficiently.
First, in the constructor, it builds a prefix array where each element stores the cumulative sum of the array up to that index. For example, for nums = [1,2,3,4], the prefix array becomes [0,1,3,6,10], where each value represents the sum of elements before it.

When we call sumRange(1,3), instead of adding elements manually (2+3+4), the code uses the formula:
👉 prefix[right+1] − prefix[left]

So here:

prefix[4] = 10 (sum of all elements)
prefix[1] = 1 (sum before index 1)

Final result = 10 − 1 = 9

This approach makes each query run in O(1) time, instead of recalculating sums every time.

---

## 2. #560 Subarray Sum Equals K

### ❓ Question

Find the total number of continuous subarrays whose sum equals `k`.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(subarraySum([1,1,1], 2))
```

### ✅ Output

```
2
```

### 💡 Explanation

Uses hashmap to track prefix sums and count valid subarrays.

This code uses the Prefix Sum + HashMap technique to count how many subarrays have sum equal to k.
Instead of checking every subarray (which is slow), it keeps track of cumulative sums (total) and stores how many times each sum has appeared in a dictionary d.

For nums = [1,1,1] and k = 2:

Start with d = {0:1} (this handles cases where subarray starts from index 0)
As we move through the array, we keep adding elements to total
At each step, we check:
👉 If (total − k) already exists in dictionary, it means a subarray with sum k is found

Step-by-step:

After first 1: total = 1 → no match
After second 1: total = 2 → (2−2=0 exists) → count = 1
After third 1: total = 3 → (3−2=1 exists) → count = 2

So total subarrays = 2

This makes the solution efficient with O(n) time complexity

---

## 3. #125 Valid Palindrome

### ❓ Question

Check whether a string is a palindrome after removing non-alphanumeric characters and ignoring case.

### 💻 Code

```python
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

### ▶️ Execution

```python
print(isPalindrome("A man, a plan, a canal: Panama"))
```

### ✅ Output

```
True
```

### 💡 Explanation

Clean string and compare it with its reverse.

This code checks whether a string is a palindrome by first cleaning the string and then comparing it with its reverse.

Step 1: It removes all non-alphanumeric characters and converts everything to lowercase:

        "A man, a plan, a canal: Panama"
        → "amanaplanacanalpanama"

Step 2: It compares the cleaned string with its reverse using:

        s == s[::-1]

Since both forward and backward strings are the same, it returns True.

Even though Python uses slicing here, logically it’s like:

    → One pointer from start
    → One pointer from end
    → Compare characters moving inward

---

## 4. #167 Two Sum II

### ❓ Question

Find two numbers in a sorted array that add up to a target.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(twoSum([2,7,11,15], 9))
```

### ✅ Output

```
[1, 2]
```

### 💡 Explanation

Two-pointer technique reduces time complexity to O(n).

This code uses the Two Pointers technique to find two numbers in a sorted array that add up to the target.

We start with:

l (left pointer) at the beginning
r (right pointer) at the end

For numbers = [2,7,11,15] and target = 9:

Step 1:
2 + 15 = 17 → too big → move right pointer left
Step 2:
2 + 11 = 13 → still big → move right pointer
Step 3:
2 + 7 = 9 → match found ✅

Return indices (1-based): [1, 2]

👉 If sum is too small → move left pointer
👉 If sum is too large → move right pointer
---

## 5. #643 Maximum Average Subarray

### ❓ Question

Find the maximum average of a subarray of length `k`.

### 💻 Code

```python
def findMaxAverage(nums, k):
    window = sum(nums[:k])
    max_sum = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        max_sum = max(max_sum, window)

    return max_sum / k
```

### ▶️ Execution

```python
print(findMaxAverage([1,12,-5,-6,50,3], 4))
```

### ✅ Output

```
12.75
```

### 💡 Explanation

Sliding window updates sum efficiently without recomputation.

This code uses the Sliding Window technique to find the maximum average of any subarray of size k.

For nums = [1,12,-5,-6,50,3] and k = 4:

First, calculate the sum of the first window (first 4 elements):
1 + 12 + (-5) + (-6) = 2

So, window = 2, max_sum = 2

🔄 Slide the Window

Instead of recalculating sum every time, we:
👉 Add next element and remove previous element

Move 1 step:
    emove 1, Add 50 → window = 2 - 1 + 50 = 51
    max_sum = 51
Move next:
    Remove 12, Add 3 → window = 51 - 12 + 3 = 42
    max_sum = 51 (unchanged)

📊 Final Maximum Sum
    max_sum = 51

✅ Average
    51 / 4 = 12.75

Instead of recalculating every subarray (O(n*k)), we update in constant time → overall O(n)
---

## 6. #3 Longest Substring Without Repeating

### ❓ Question

Find the length of the longest substring without repeating characters.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(lengthOfLongestSubstring("abcabcbb"))
```

### ✅ Output

```
3
```

### 💡 Explanation

Sliding window ensures all characters are unique.

This code uses the Sliding Window technique to find the length of the longest substring without repeating characters.

For s = "abcabcbb":

We use:

l → left pointer
r → right pointer
char_set → stores unique characters in current window


🔄 Step-by-Step
Start:
    Window = ""

Add a → "a" → length = 1
Add b → "ab" → length = 2
Add c → "abc" → length = 3 

Next a (duplicate):
👉 Remove from left until duplicate is gone

    Remove 'a' → Window becomes "bc"
    Add 'a' → Window = "bca"

Continue:

    "cab" → length = 3
    "abc" → length = 3

When duplicates like b appear:
👉 Keep removing from left

Expand window → if duplicate found, shrink from left → track max length
Each character is added and removed at most once → overall O(n) time

---

## 7. #141 Linked List Cycle

### ❓ Question

Detect if a linked list contains a cycle.

### 💻 Code

```python

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

### ▶️ Execution

```python
head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node2.next = head

print(hasCycle(head))
```

### ✅ Output

```
True
```

### 💡 Explanation

Fast pointer meets slow pointer if a cycle exists.

This code uses the Fast & Slow Pointer technique (also called Floyd’s Cycle Detection) to check if a linked list has a cycle.

We use:

slow pointer → moves 1 step at a time
fast pointer → moves 2 steps at a time

How It Works

If there is a cycle:
👉 the fast pointer will eventually catch up to the slow pointer

Linked list created:

        1 → 2
        ↑   ↓
        ← ← ←

👉 Node 2 points back to Node 1 → cycle exists

Step-by-step:
    Start: slow = 1, fast = 1
    Move:
        slow → 2
        fast → 1 (jumps 2 steps due to cycle)

👉 Now both meet → cycle detected ✅

👉 If fast pointer meets slow pointer → cycle exists

No extra memory needed → runs in O(n) time and O(1) space
---

## 8. #876 Middle of Linked List

### ❓ Question

Return the middle node of a linked list.

### 💻 Code

```python

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

### ▶️ Execution

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(middleNode(head))
```

### ✅ Output

```
3
```

### 💡 Explanation

Fast moves twice → slow lands at middle.

This code finds the middle node of a linked list using the Fast & Slow Pointer technique.

We use:

slow pointer → moves 1 step at a time
fast pointer → moves 2 steps at a time

🔄 How It Works

As fast moves faster, when it reaches the end of the list,
👉 slow will be exactly at the middle node


Linked list:   1 → 2 → 3 → 4

Step-by-step:

Start: slow = 1, fast = 1
Move:
    slow → 2
    fast → 3
Move again:
    slow → 3
    fast → None (end reached)

👉 Loop stops → slow is at 3


Fast moves 2 steps, slow moves 1 → slow reaches middle

Runs in O(n) time and O(1) space
---

## 9. #206 Reverse Linked List

### ❓ Question

Reverse a singly linked list.

### 💻 Code

```python

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

### ▶️ Execution

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

rev = reverseList(head)
while rev:
    print(rev.val, end=" ")
    rev = rev.next
```

### ✅ Output

```
3 2 1
```

### 💡 Explanation

Reverses links using previous pointer.

This code reverses a singly linked list using in-place pointer manipulation.

We use three pointers:

    curr → current node
    prev → previous node (initially None)
    nxt → stores next node temporarily

🔄 How It Works

    We go node by node and reverse the direction of links

Original list:  1 → 2 → 3 → None

Step-by-step:

Step 1:
        curr = 1
        Reverse → 1 → None

Step 2:
        curr = 2
        Reverse → 2 → 1 → None

Step 3:
        curr = 3
        Reverse → 3 → 2 → 1 → None

✅ Final Reversed List
        3 → 2 → 1


👉 Reverse each node’s next pointer to point backward

We keep shifting pointers so the list direction flips step by step.

---

## 10. #92 Reverse Linked List II

### ❓ Question

Reverse nodes between positions `left` and `right`.

### 💻 Code

```python

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

### ▶️ Execution

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

res = reverseBetween(head, 2, 3)
while res:
    print(res.val, end=" ")
    res = res.next
```

### ✅ Output

```
1 3 2 4
```

### 💡 Explanation

Reverses only part of the list using pointer adjustments.

This code reverses only a part of a linked list (from position left to right) using in-place pointer manipulation.

Input list:  1 → 2 → 3 → 4

Reverse from position 2 to 3

🔄 How It Works

1️⃣ A dummy node is used to handle edge cases easily
2️⃣ prev moves to the node just before the reversal starts
3️⃣ Then we repeatedly take the next node and move it to the front of the sublist

🔁 Step-by-step

Initial: 
        1 → 2 → 3 → 4
            ↑   ↑
          left right

Step 1:
Take node 3 and move it before 2

1 → 3 → 2 → 4

(Only one iteration needed since right-left = 1)


✅ Final List
1 → 3 → 2 → 4

👉 Pick nodes one by one and insert them at the front of the selected range

Instead of reversing entire list, we only rearrange pointers inside the given range. 

Efficiency : Time: O(n)  , Space: O(1)
---

## 11. #496 Next Greater Element I

### ❓ Question

Find next greater element for each element in nums1.

### 💻 Code

```python
def nextGreaterElement(nums1, nums2):
    stack = []
    d = {}

    for n in nums2:
        while stack and stack[-1] < n:
            d[stack.pop()] = n
        stack.append(n)

    return [d.get(x, -1) for x in nums1]
```

### ▶️ Execution

```python
print(nextGreaterElement([4,1,2],[1,3,4,2]))
```

### ✅ Output

```
[-1, 3, -1]
```

### 💡 Explanation

Monotonic stack tracks next greater values efficiently.

This code finds the next greater element for each value in nums1 using a Monotonic Stack.

👉 The idea:
For every element in nums2, find the first greater element to its right


Eg: 
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

🔄 Step-by-step (Processing nums2)

We use:
        stack → keeps elements in decreasing order
        d → stores next greater mapping

Start:
        stack = []
        d = {}

Take 1 → push
    stack = [1]

Take 3
    👉 3 > 1 → so next greater of 1 is 3
    
    d = {1:3}
    stack = [3]

Take 4
    👉 4 > 3 → next greater of 3 is 4
    
    d = {1:3, 3:4}
    stack = [4]

Take 2
    👉 2 < 4 → just push

    stack = [4,2]

(No greater element for 4 and 2 → they remain)

📊 Mapping Created
    d = {1:3, 3:4}

🔁 Build Result for nums1
    nums1 = [4,1,2]

4 → no greater → -1  
1 → 3  
2 → no greater → -1  

✅ Output
[-1, 3, -1]

👉 Use stack to track decreasing elements → when a bigger number comes, resolve previous elements

Each element is pushed and popped at most once → O(n) time
---

## 12. #739 Daily Temperatures

### ❓ Question

Find number of days until a warmer temperature.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
```

### ✅ Output

```
[1,1,4,2,1,1,0,0]
```

### 💡 Explanation

Stack helps track next warmer day.

This code finds how many days you must wait to get a warmer temperature using a Monotonic Stack.

👉 Instead of checking every future day, we store indices of days in a stack and resolve them when a warmer day appears.

T = [73,74,75,71,69,72,76,73]


🔄 How It Works

We use:
        stack → stores indices of days (not values)
        res → result array initialized with 0

Step-by-step

Day 0 → 73 → push index
    stack = [0]

Day 1 → 74
    👉 74 > 73 → warmer day found
    res[0] = 1 (1-0)
    stack = []
Push index 1

Day 2 → 75
    👉 75 > 74
    res[1] = 1

Day 3 → 71 → push
Day 4 → 69 → push

Day 5 → 72
    👉 72 > 69 → res[4] = 1
    👉 72 > 71 → res[3] = 2


Day 6 → 76
    👉 resolves multiple previous days
    res[5] = 1
    res[2] = 4

Day 7 → 73 → no warmer future → stays 0

✅ Final Output
[1,1,4,2,1,1,0,0]


👉 Store indices → when warmer day comes, calculate difference

Each index is pushed and popped once → O(n) time
---

# 🔹 PART – B (Fully Complete)

*(Same structure continues — omitted here for brevity? No — you required 100%, so continuing below)*

---

## 1. #238 Product of Array Except Self

### ❓ Question

Return array where each element is product of all elements except itself.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(productExceptSelf([1,2,3,4]))
```

### ✅ Output

```
[24, 12, 8, 6]
```

### 💡 Explanation

Uses prefix and suffix products.

This code finds the product of all elements except itself without using division, using a Prefix (Left) + Suffix (Right) approach.

Example
        nums = [1,2,3,4]

        Goal:   [2×3×4, 1×3×4, 1×2×4, 1×2×3]
                → [24, 12, 8, 6]


🔄 How It Works

We calculate in two passes:

1️⃣ Left Product Pass
res = [1,1,1,1]

Build product of elements to the left:

res[0] = 1
res[1] = 1
res[2] = 2
res[3] = 6

👉 After left pass:

res = [1,1,2,6]


2️⃣ Right Product Pass

Now multiply with right side products:

Start from right:

res[3] = 6 * 1 = 6
res[2] = 2 * 4 = 8
res[1] = 1 * 12 = 12
res[0] = 1 * 24 = 24

✅ Final Result
[24, 12, 8, 6]

👉 For each index: multiply left product × right product

Two passes only → O(n) time , Constant extra space → O(1)
---

## 2. #11 Container With Most Water

### ❓ Question

Find max water container area.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(maxArea([1,8,6,2,5,4,8,3,7]))
```

### ✅ Output

```
49
```

### 💡 Explanation

Two pointers maximize area efficiently.

This code finds the maximum water container area using the Two Pointers technique.

👉 The idea:
Water stored = min(height[left], height[right]) × width

🔍 Example
height = [1,8,6,2,5,4,8,3,7]


🔄 How It Works

We start with:
            l → left pointer (start)
            r → right pointer (end)

Step-by-step
Step 1:
    l=0 (1), r=8 (7)
    Area = min(1,7) × 8 = 8

Move left (smaller height)

Step 2:
    l=1 (8), r=8 (7)
    Area = min(8,7) × 7 = 49 

Continue moving pointers:

👉 Always move the smaller height pointer
(because bigger height won’t help if smaller limits water)

📊 Maximum Area Found : 49

👉 Area = min(height) × width
👉 Move pointer with smaller height

We try to maximize height while reducing width smartly → O(n) instead of O(n²)


---

## 3. #424 Longest Repeating Character Replacement

### ❓ Question

Find longest substring with same characters after at most k replacements.

### 💻 Code

```python
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

### ▶️ Execution

```python
print(characterReplacement("AABABBA", 1))
```

### ✅ Output

```
4
```

### 💡 Explanation

Sliding window maintains valid substring size.

This code finds the longest substring where we can make all characters the same using at most k replacements, using the Sliding Window technique.

🔍 Example :  s = "AABABBA", k = 1

🔄 How It Works

We maintain:
    l → left pointer
    r → right pointer
    count → frequency of characters in window
    maxf → count of most frequent character in window

🧠 Key Idea In a window:

    window size - most frequent character ≤ k

Means we can convert all other characters to the most frequent one.

👉 Step-by-step 
Build window "AAB"
    maxf = 2 (A)
    window = 3 → valid

Expand "AABA"
    maxf = 3
    window = 4 → valid

Expand "AABAB"
    window = 5, maxf = 3
    5 - 3 = 2 > k → invalid

👉 Shrink from left

📊 Maximum Length Found : 4

👉 Keep window valid using (window size − max frequency ≤ k)
👉 Expand → shrink when invalid

Each character processed once → O(n) time
---

## 4. #19 Remove Nth Node From End

### ❓ Question

Remove nth node from end of list.

### 💻 Code

```python

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

### ▶️ Execution

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

res = removeNthFromEnd(head, 2)
while res:
    print(res.val, end=" ")
    res = res.next
```

### ✅ Output

```
1 3
```

### 💡 Explanation

Two-pointer gap helps locate node before deletion.

This code removes the Nth node from the end of a linked list using the Fast & Slow Pointer technique.


Example : 
        Linked List:  1 → 2 → 3    
        n = 2
👉 Remove the 2nd node from end → node 2


🔄 How It Works , We use:

    fast pointer
    slow pointer
    dummy node (to handle edge cases like removing head)

Step 1: Move fast pointer n steps
    fast moves 2 steps ahead

Step 2: Move both pointers
Move fast and slow together until fast reaches the end:
    fast → end  
    slow → node before the one to delete

Step 3: Remove node
    slow.next = slow.next.next
👉 This skips (removes) the target node

🔁 Result List : 1 → 3

👉 Keep gap of n between fast & slow → slow reaches node before deletion
    Fast reaches end first → slow lands at correct position
---

## 5. #61 Rotate List

### ❓ Question

Rotate linked list to the right by k positions.

### 💻 Code

```python

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

### ▶️ Execution

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

res = rotateRight(head, 1)
while res:
    print(res.val, end=" ")
    res = res.next
```

### ✅ Output

```
3 1 2
```

### 💡 Explanation

Convert to circular list, then break at correct point.

This code rotates a linked list to the right by k positions using pointer manipulation.

Example :
        Linked List: 1 → 2 → 3
        k = 1

👉 After rotation:
        3 → 1 → 2

🔄 How It Works :
1️⃣ Find Length and Tail
    length = 3
    tail = node 3

2️⃣ Optimize k
    k = k % length = 1 % 3 = 1
👉 (Avoid unnecessary full rotations)

3️⃣ Make List Circular
    tail.next = head

    1 → 2 → 3
    ↑       ↓
    ← ← ← ← ←

4️⃣ Find New Tail
    steps = length - k = 3 - 1 = 2
Move 2 steps:
    new_tail = node 2

5️⃣ Break the Circle
    new_head = node 3
    new_tail.next = None

✅ Final List
    3 → 1 → 2


👉 Make list circular → break at correct point
    Rotating right is equivalent to shifting break point in circular list.

---

## 6. #901 Online Stock Span

### ❓ Question

Calculate stock span for each day.

### 💻 Code

```python
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

### ▶️ Execution

```python
sp = StockSpanner()
print(sp.next(100))
print(sp.next(80))
print(sp.next(60))
print(sp.next(70))
print(sp.next(60))
print(sp.next(75))
print(sp.next(85))
```

### ✅ Output

```
1
1
1
2
1
4
6
```

### 💡 Explanation

This code calculates the stock span using a Monotonic Stack.

👉 Stock span = number of consecutive days (including today) where price ≤ today’s price.


Example : 
    Prices sequence: 100, 80, 60, 70, 60, 75, 85

🔄 How It Works

We use a stack that stores:
    (price, span)

👉 The stack keeps prices in decreasing order

Step-by-step
Price = 100
    stack = [(100,1)]
    span = 1

Price = 80
    80 < 100 → push
    span = 1

Price = 60
    60 < 80 → push
    span = 1

Price = 70
👉 70 > 60 → pop
    span = 1 + 1 = 2

Price = 60
    push → span = 1

Price = 75
👉 pop 60, 70
    span = 4

Price = 85
👉 pop 75, 80
    span = 6

✅ Output
1
1
1
2
1
4
6


👉 Pop all smaller prices and add their spans
    We combine previous spans to avoid re-checking → efficient merging

Each element pushed & popped once → O(n) , Space: O(n)