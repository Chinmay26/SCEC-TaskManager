import subprocess

class ssh_client:
  def __init__(self, host):
		self. host = host

	def execute_command(self, command, op_file, err_file):
    try:
	    result = subprocess.Popen(["ssh", self.host, command], shell=False, 
                                stdout=op_file, stderr=err_file)
    except SubprocessError:
      #TO-DO :Handle excpetion
			#should we retry ? or raise another custom exception
			pass
