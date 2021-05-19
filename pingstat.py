####
# pingstat - pings hosts and puts them into a database
# This program needs to be run as root (due to ping)
####

import sqlops as sops
import netops as nets

if __name__ == '__main__':

  sops.createSqlLiteDb()
  #sops.insertTestData()
  sops.readTableData()

  nets.pingDns()