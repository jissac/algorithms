# useful_info
Good to know stuff

[EPE Big Data Analytics group getting started info](https://github.ford.com/EPE-BigDataAnalytics/GettingStarted)

## Github SSH keys in WSL
`ssh-keygen`     
Hit Enter 3 times      
`Your identification has been saved in /home/jissac3/.ssh/id_rsa.`         
`Your public key has been saved in /home/jissac3/.ssh/id_rsa.pub.`     
copy the created .ssh directory `Created directory '/home/jissac3/.ssh'.` to current directory: `cp -r /home/jissac3/.ssh/ .`      
print out id_rsa.pub: `cat id_rsa.pub` and copy entire output into github SSH keys: https://github.ford.com/settings/keys

## Use WSL to access cluster
`ssh cluster_name`
## Cluster names
**PROD:** hpchdp2e.hpc.ford.com      
**DEV_QA:** hpchdd2e.hpc.ford.com       
**POC:** hpchd1e.hpc.ford.com       
**DR:** hpchdr2e.hpc.ford.com

## Permissions on the cluster
`chmod -R 777 zeppelin-0.8.1-bin-all` ( full read, write, and execute permissions via chmod 777 on every file in the directory you ran the command on and due to the -R (recursive) switch every file in every directory under that)


`pgrep -u jissac3 -lf ssh`: pgrep looks through the currently running processes and lists the process IDs which matches the selection criteria to stdout.                    

`ps -aux | grep jissac3`: The ps Command. The ps (i.e., process status) command is used to provide information about the currently running processes, including their process identification numbers (PIDs). A process, also referred to as a task, is an executing (i.e., running) instance of a program.         


`pkill -9 -u jissac3 -f zeppelin`: kills all processes matching zeppelin, regardless of PID.

`pgrep -u jissac3 -lf zeppelin`: check if process still running

## Copy packages from one conda env to another
`conda list --export > package_list.txt`        
`while read requirement; do conda install --yes $requirement; done < package_list.txt`

## Sharepoints
BDD: https://com.spt.ford.com/sites/BigDataDrive/default.aspx           
HA: https://pd1.spt.ford.com/sites/HA/Shared%20Documents/Forms/AllItems.aspx        

## Currently running jobs on Hadoop
http://hpchdp2.hpc.ford.com:8088/cluster/apps/RUNNING

## Kill application on Hadoop
`yarn application -list`                                   
`yarn application -kill application_1553350019942_1037902`                 
or        
`mapred job -list`           
`mapred job -kill <jobId>`                 

## Run HQL query in HDFS
`hive -f filename.hql`           

## Run HQL query in HDFS and save to external file
beeline --outputformat=csv2 -f /s/jissac3/UM_FCW_query.hql >/s/jissac3/UM_FCW.csv

## Check file size in HDFS
hdfs dfs -du -s -h [filepath]
