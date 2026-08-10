ping cimsdev01-scan.yellow.com
PING cimsdev01-wteex-scan.ocisbcimsoracl.ocivnetwestusm.oraclevcn.com (10.29.95.175) 56(84) bytes of data.
64 bytes from 10.29.95.175 (10.29.95.175): icmp_seq=1 ttl=60 time=2.58 ms
64 bytes from 10.29.95.175 (10.29.95.175): icmp_seq=2 ttl=60 time=2.20 ms
64 bytes from 10.29.95.175 (10.29.95.175): icmp_seq=3 ttl=60 time=2.25 ms
64 bytes from 10.29.95.175 (10.29.95.175): icmp_seq=4 ttl=60 time=2.57 ms
64 bytes from 10.29.95.175 (10.29.95.175): icmp_seq=5 ttl=60 time=15.4 ms
64 bytes from 10.29.95.175 (10.29.95.175): icmp_seq=6 ttl=60 time=1.97 ms
^C
--- cimsdev01-wteex-scan.ocisbcimsoracl.ocivnetwestusm.oraclevcn.com ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 5008ms
rtt min/avg/max/mdev = 1.968/4.498/15.422/4.890 ms
[root@vm-mms-cims02 TestQaConn]# nping --tcp -p 1521 10.29.95.175

Starting Nping 0.7.92 ( https://nmap.org/nping ) at 2026-07-22 12:59 PDT
SENT (0.0170s) TCP 10.15.128.5:11505 > 10.29.95.175:1521 S ttl=64 id=36087 iplen=40  seq=3863118574 win=1480
RCVD (0.0196s) TCP 10.29.95.175:1521 > 10.15.128.5:11505 SA ttl=60 id=0 iplen=44  seq=840734935 win=62720 <mss 1410>
SENT (1.0177s) TCP 10.15.128.5:11505 > 10.29.95.175:1521 S ttl=64 id=36087 iplen=40  seq=3863118574 win=1480
RCVD (1.0199s) TCP 10.29.95.175:1521 > 10.15.128.5:11505 SA ttl=60 id=0 iplen=44  seq=856364646 win=62720 <mss 1410>
^C
Max rtt: 2.474ms | Min rtt: 2.172ms | Avg rtt: 2.323ms
Raw packets sent: 2 (80B) | Rcvd: 2 (92B) | Lost: 0 (0.00%)
Nping done: 1 IP address pinged in 1.85 seconds
[root@vm-mms-cims02 TestQaConn]# cat testQaConn.py
import oracledb

# -----------------------------
# EDIT THESE VALUES "HOST:PORT/SERVICE"
# -----------------------------
dsn = "cimsdev01-scan.yellow.com:1521/ECSQA.ocisbcimsoracl.ocivnetwestusm.oraclevcn.com";     # Example: "10.10.10.5:1521/ORCL"
username = "ssctt1i"
password = "asdf#"
# -----------------------------

def main():
    try:
        print("Attempting Oracle connection...")
        conn = oracledb.connect(user=username, password=password, dsn=dsn)
        print("Connection successful")
        conn.close()
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    main()
