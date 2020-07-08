import speedtest
import fourletterphat as flp

servers = []

flp.scroll_print("STARTING TEST")
flp.show()

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

flp.print_str("DOWN")
flp.show()

s.download()

flp.print_str("UP")
flp.show()

s.upload()

print("Test complete!")
