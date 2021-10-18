# ip-address-handler-test
A test for fast runtime approach


# What would you do differently if you had more time?
R: I will use a service with a high read performance such a redis or elastic search
# What is the runtime complexity of each function?
R:
`request_handled` uses a Hashmap (dictionary) and its runtime complexity is O(1).
Also they uses a Double linked list to store the top ip recurrences, 
its runtime complexity inserting a node is O(1) if its new, otherwise the worst case is O(n)
`top100` its runtime complexity is O(n), by converting the node into a easy read list of elements.


# How does your code work?
- `request_handled` does the 90% of the job by inserting into the Hashmap `ips` to store values and references 
and keep updated the Double Linked List called (`top_ips`) by max recurrences, 
- Decouple nodes in linked list `top_ips` if length surpass the `max_length` defined by 100 
or replace the last element if current node is frequency higher.
- The Hashmap `ips` the key is `ip_address` and its data structure contains current frequency and 
a reference of the element (`NodeItem`) of `top_ips`. 
- This list avoid to repeatly searching the current node each time a request is received 
- and just swap nodes connected nearby or insert in the tail of the list.
- The Double linked list `top_ips` is always ordered by recurrence, so when the top100 is called, 
it just loop through elements to store in a proper simple list is returned.
# What other approaches did you decide not to pursue?
R: Using a heap sorted by máx frequency in root and group elements with same frequency.
Its worst case will be all ip address receive could have same frequency
(but in a real environment scenario is unlikely).
And top100 function should merge all lists from root to the subtree with higher frequency 
and then chop it when it reachs 100 or more elements.
When a node changes its frequency, it would be hard to exchange among nodes and lists so I drop this approach.
# How would you test this?
- First I will check if execute time is fine with requirements using `timeit`.
- I will assert a few use cases ip in different order and frequencies.