import nmap

def full_port_scan(target_ip):
   nm = nmap.PortScanner()
   nm.scan(target_ip, '1-65535', arguments='-T5','-vv','-Pn','--min-rate=1000')
   open_ports = [port for port in nm[target_ip['tcp'] if nm[target_ip]['tcp'][port]['state'] == 'open']
   return open_ports


def aggressive_scan(target_ip, ports):
   nm = nmap.PortScanner()
   open_ports_str = ','.join(map(str,ports))
   nm.scan(target_ip, open_ports_str, arguments''-A','-sCV','-T4',-Pn)
   return nm

def save_to_file(scan_results,file_name):
   with open(file_name, 'w') as file:
   file.write(scan_results)

def main ():
   target_ip = input('Enter the target IP address: ')
   print(f'Starting full port scan on {target_ip}... ')
   open_ports = full_port_scan(target_ip)
   print(f'Open ports: {open_ports}')
   print('Starting aggressive scan on open ports... ')
   scan_results = aggressive_scan(target_ip, open_ports)
   scan_output = scan_results.csv()
   output_file = 'nmap-all-tcp.nmap'
   save_to_file(scan_output, output_file)
   print(f'Scan results saved to {output_file}')


if __name__ == '__main__':
main()
