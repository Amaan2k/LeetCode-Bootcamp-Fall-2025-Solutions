class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know, share = deque([(1, 1)]), deque([])
        k_count, s_count = 1, 0

        for i in range(2, n + 1):
            if know and know[0][0] == i - delay:
                k_count -= know[0][1]
                s_count += know[0][1]
                share.append(know[0])
                know.popleft()

            if share and share[0][0] == i - forget:
                s_count -= share[0][1]
                share.popleft()

            if share:
                k_count += s_count
                know.append((i, s_count))

        return (k_count + s_count) % (10**9 + 7)