from datetime import datetime

date = datetime.today()
print(
    f"Seconds since January 1, 1970: {date.timestamp():,.4f} or {date.timestamp():.2e} in scientific notation"
)
print(date.strftime("%b %d %Y"))
