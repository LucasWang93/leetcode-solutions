# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy = ListNode(-1)
        # p = dummy
        # pq = []

        # for i, head in enumerate(lists):
        #     if head:
        #         heapq.heappush(pq, (head.val, i, head))

        # while(pq):
        #     _, i, node = heapq.heappop(pq)
        #     p.next = node
        #     if node.next:
        #         heapq.heappush(pq, (node.next.val, i, node.next))
        #     p = p.next
        # return dummy.next

        dummy = ListNode(-1)
        p = dummy

        pq = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        
        while(pq):
            _, i, node = heapq.heappop(pq)

            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))

            p = p.next

        return dummy.next