from collections import Counter
s = "leetcode"
t = "practice"

# counter(t) = {p:1 r:1 a:1 c:2 t:1 i:1 e:1 }
# counter(s) = {l:1 e:3 t:1 c:1 o:1 d:1 }
sum((Counter(t)-Counter(s)).values())

# Counter(t) - Counter(s) =  {p:1  r:1  a:1  c:2-1=>1  t:1-1=>0  i:1  e:1-3=>-2=>0 }
# (Counter(t)-Counter(s)).values() = 1  1  1        1         0    1         0
# sum((Counter(t)-Counter(s)).values()) = 1 + 1 + 1 + 1 + 1 => 5


# Example 1:

# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
# Example 2:

# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
# Example 3:

# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 
