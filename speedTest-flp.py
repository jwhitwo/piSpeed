import speedtest

servers = []

print("Getting servers...")

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
print("Server selected. Testing download...")
s.download()
print("Download complete. Testing upload.")
s.upload()

print(s.results.dict())

print("Test complete!")
