
import time

import sublime_plugin


class MandocNewCommand(sublime_plugin.WindowCommand):
	def run(self):
		new_file = self.window.new_file()
		new_file.set_syntax_file("Packages/Mandoc/Mandoc.sublime-syntax")
		new_file.run_command("insert_snippet", {"contents": """\
.\\" ${{1:name}}(${{2:section_num}}) man page
.\\" Written in Mandoc, refer to mdoc(7) for further info
.Dd {}
.Dt ${{1/[[:alpha:]]/\\u$&/g}} ${{2}}
.Os
.Sh NAME
.Nm ${{1}}
.Nd ${{0:description}}
""".format(time.strftime("%B %d, %Y"))})
