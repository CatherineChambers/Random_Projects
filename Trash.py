# import random
# import time
# import numpy as np
#
# start_time = time.perf_counter()
# ys = []
# for rep in range(1000000):
#     y = 0
#     for k in range(10):
#         x = random.choice([1, 2, 3, 4, 5, 6])
#         y = y + x
#     ys.append(y)
# end_time = time.perf_counter()
# print(end_time - start_time)
#
# start_time = time.perf_counter()
# X = np.random.randint(1, 7, (1000000, 10))
# Y = np.sum(X, axis=1)
# end_time = time.perf_counter()
# print(end_time - start_time)
