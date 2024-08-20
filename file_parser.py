import csv

# ## We are maping protocol number to protocol, we can use any other list or library to get protocol_name as well to map this is written according to the example providen. 
def map_protocol(port_num: int)->str:
   protocol_name={6:"tcp",1:"icmp",17:"udp",80:"HTTP",443:"HTTPS",21:"FTP",25:"SMTP",110:"POP3",143:"IMAP"}
   if port_num in protocol_name:
      return protocol_name[port_num]
   else:
      return "None"
   

## Created a funnction to check lookup table and return the matching tag if not returning Untagged
def lookup_table(dst_port: int,protocol: str, input_file):
  with open(input_file,'r') as lookup:
    reader=csv.DictReader(lookup)
    for r in reader:
      #print(r['dstport'])
      if int(r['dstport'])==dst_port and r['protocol']==protocol:
        return r['tag']
    else:
      return "Untagged"

## This is the MAIN function which calls the above two functions. Additionally we are using with as it automatically closes the file when the block is exited
def log_mapping(input_file,input_with_tag):
  modified_lines=[]
  count_tags={}
  port_protocol_count={}
  with open(input_file,'r+') as f_in:
    #fieldnames=['Destination_port', 'Protocol']
    for line in f_in:
      fields=line.split()
      data={
          'dst_port':int(fields[6]),
          'protocol':map_protocol(int(fields[7]))
      }
      # Part 1 file containing tag mappings are plain text (ascii) files 
      ## Created new text with tags to avoid any doing any changes in iput file(original file)
      tag=lookup_table(data['dst_port'],data['protocol'],'lookup_table.csv')
      # used rstrip to avoid any unnecessory spacing 
      modified_lines.append(line.rstrip()+f" {tag}\n")


      ## Part 2 Count of matches for each tag, 
      if tag in count_tags:
        count_tags[tag]+=1
      else:
        count_tags[tag]=1
      
      ## Part 3 Count of matches for each port/protocol combination 
      if (data['dst_port'],data['protocol']) in port_protocol_count:
          port_protocol_count[(data['dst_port'],data['protocol'])]+=1
      else:
          port_protocol_count[(data['dst_port'],data['protocol'])]=1
  with open(input_with_tag,'w') as f_out:
    f_out.writelines(modified_lines)
  return count_tags,port_protocol_count



## Creating a new CSV file named output.csv to save the output file with both the outputs
def save_both_outputs(count_tags,port_protocol_count):
  with open("output.csv",'w',newline='') as f_out:
    writter=csv.writer(f_out)
    writter.writerow(['Tag','Count'])
    for k,v in count_tags.items():
      writter.writerow([k,v])

    # Adding new line to differentiate between both the outputs

    writter.writerow([]*5)

    writter.writerow(['Port','Protocol','Count'])

    for k,v in port_protocol_count.items():
      writter.writerow([k[0],k[1],v])

input_file='test.txt'
taged_output='taged_output.txt'
count_tags,port_protocol_count=log_mapping(input_file,input_with_tag=taged_output)
save_both_outputs(count_tags,port_protocol_count)