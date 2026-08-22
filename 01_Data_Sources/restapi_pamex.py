import http.client

conn = http.client.HTTPSConnection("gateway.api.bot.or.th")

headers = {
    'Accept': "*/*",
    'Authorization': "eyJvcmciOiI2NzM1NzgwZWM4YzFlYjAwMDEyYTM3NzEiLCJpZCI6IjQ3MDkwODdjMTU0NDQyYjQ4Y2YyMmI5NmFmMzRkZmRjIiwiaCI6Im11cm11cjEyOCJ9"
}

conn.request("GET", "/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/?start_period=2026-08-20&end_period=2026-08-22", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))