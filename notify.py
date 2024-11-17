import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
      title = "arch",
      message = "arch",
      timeout = 30
    )
    time.sleep(10)