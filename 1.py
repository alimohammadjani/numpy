import numpy as np
from datetime import datetime, timedelta
customer_id=np.random.randint(1, 501, size=100)
product_id=np.random.randint(1, 51, size=100)
price=np.random.uniform(5, 501, size=100)
quantity=np.random.randint(1, 6, size=100)
start = datetime(2025, 8, 1)
end = datetime(2025, 8, 31, 23, 59, 59)
timestamp=[start + timedelta(seconds=np.random.randint(0, int((end-start).total_seconds()))) for _ in range(100)]
mean,sum=np.mean(price),np.sum(price)
max_price=np.max(price)
peak_time=timestamp[max(timestamp,return_count=True)]