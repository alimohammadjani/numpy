import numpy as np
from datetime import datetime, timedelta
from collections import Counter
customer_id = np.random.randint(1, 501, size=100)
product_id = np.random.randint(1, 51, size=100)
price = np.random.uniform(5, 501, size=100)
quantity = np.random.randint(1, 6, size=100)
start = datetime(2025, 8, 1)
end = datetime(2025, 8, 31, 23, 59, 59)
timestamp = [start + timedelta(seconds=np.random.randint(0, int((end-start).total_seconds()))) for _ in range(100)]
mean_price = np.mean(price)
sum_price = np.sum(price)
max_price = np.max(price)
peak_time = Counter(timestamp).most_common(1)[0][0]
print(f"Mean price: {mean_price:.2f}")
print(f"Total price: {sum_price:.2f}")
print(f"Max price: {max_price:.2f}")
print(f"Most frequent purchase time: {peak_time}")