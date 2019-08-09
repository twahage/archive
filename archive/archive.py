import argparse, os, re, sys, grp, pwd, logging, logging.handlers
from os.path import expanduser
from os import walk


def main():
  parser = argparse.ArgumentParser(description='Archive files into a certain destination folder.')
  parser.add_argument('groups', metavar='G',  nargs='+',
                     help='the group of the users, whose files should be moved (OR junction is used for multiple groups)')
  parser.add_argument('--dest', required=True, 
                     help='the destination folder')
  parser.add_argument('--src', default='.',
                     help='the source folder. If not specified, the cwd will be used')

  args = parser.parse_args()

  #logger configuration
  loggingfilepath=expanduser("~/.pyarchive/system.log")
  if not os.path.exists(os.path.dirname(loggingfilepath)):
      try:
        os.makedirs(os.path.dirname(loggingfilepath))
      except:
        print "ERROR! Could not create log file directory at " + os.path.dirname(loggingfilepath) + " ... Exiting."
        sys.exit()
        
  handler = logging.handlers.WatchedFileHandler(loggingfilepath)
  formatter = logging.Formatter(logging.BASIC_FORMAT)
  handler.setFormatter(formatter)
  rootLogger = logging.getLogger()
  rootLogger.setLevel("INFO")
  rootLogger.addHandler(handler)

  print "Logging to " + expanduser(loggingfilepath)

  #get the list of all users in the mentioned groups
  userlist=[]
  usernames=[]

  for group in args.groups:
    try:  
      g=grp.getgrnam(group)
      for person in g.gr_mem:
        p=pwd.getpwnam(person) 
        userlist.append(p[2])
        usernames.append(p[0])
    except:
      print "ERROR! Group " + g + " could not be found... Exiting."
      sys.exit()

  #walk the tree
  for (dirpath, dirnames, filenames) in walk(args.src):

    for filename in filenames:
      #ignore swap and lock files as well as the script itself
      z = re.match("((.*)\.((swp)|(swo)|(apylock)))|archive\.py", filename)

      if not z:

        lockfilename=filename + ".apylock" 
        lockfilepath=dirpath + "/" + lockfilename
        filepath=dirpath + "/" + filename
        #filedestpath="./" + args.dest + "/" + filename
        filedestpath=args.dest + "/" + filename
        try:
          #create file lock
          lock_fd=os.open(lockfilepath,os.O_CREAT|os.O_EXCL|os.O_RDWR) 

          #move file
          if os.path.exists(filepath): 
            stat_info=os.stat(filepath)
            uid = stat_info.st_uid
          
            #move file only if it belongs to a user that is a member of one of the specified groups
            if uid in userlist:
              logging.info("Archive file " + os.path.abspath(filepath) + " to " + os.path.abspath(filedestpath))
              os.rename(filepath, filedestpath)

          #remove file lock
          os.close(lock_fd)
          os.remove(lockfilepath)
          lock_fd=None
        except:
           continue

if __name__=='__main__':
  main()
