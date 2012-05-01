#!/usr/bin/python

##
# create a empty project in current directory
# with autoconf tools
#
import os
import sys
import re
## declaring of functions
def mkdir(dir):
	"""make a directory if not exists"""
	if not os.path.exists(dir):
		os.makedirs(dir)


# check the input arguments
if len(sys.argv) != 5:
	print 'Usage: makeEmpytProject from ProjectName Version Email.'
	exit(1)

fromwhere = sys.argv[1]
project = sys.argv[2]
version = sys.argv[3]
email = sys.argv[4]

# make the directories of project
mkdir(project)
os.chdir(project)
mkdir('include')
mkdir('src')
mkdir('test')
mkdir('build')
mkdir('doc')
mkdir('scripts')

# generate configure.ac
print("Generating configure.ac...")
os.system('autoscan')

cmd = "sed 's/FULL-PACKAGE-NAME/" + project + "/; "
cmd += "s/VERSION/" + version + "/; "
cmd += "s/BUG-REPORT-ADDRESS/" + email + "/; "
cmd += "/AC_INIT/ a\\" + "\nAC_CONFIG_SRCDIR([])\\nAM_INIT_AUTOMAKE(" + \
	   project + ", " + version + ")\\nAC_CONFIG_HEADERS([config.h])\n"
cmd += "/Checks for programs/ aAC_PROG_CXX\\nAC_PROG_RANLIB\\n"
cmd += "AC_ARG_ENABLE(debug, [  --enable-debug\tEnable DEBUG output. ],\\n"
cmd += "\t[ CXXFLAGS=\"-g2 -O0 -DDEBUG -Wall -Werror -std=c++0x\" ],\\n"
cmd += "\t[ CXXFLAGS=\"-O3 -Wall -Werror -std=c++0x\" ])\n"
cmd += "/AC_OUTPUT/ i\\" + "AC_CONFIG_FILES([Makefile src/Makefile test/Makefile])"
cmd += "' <configure.scan >configure.ac"
os.system(cmd)

os.remove('autoscan.log')
os.remove('configure.scan')
		
# generate automake.am
print("Generating Makefile.am...")
am = open('Makefile.am', 'w')
am.write('SUBDIRS = src test\nEXTRA_DIST = include')
am.close()
os.chdir('test')
am = open('Makefile.am', 'w')
am.write('INCLUDES = -I$(top_srcdir)/include\n' +
		 'noinst_PROGRAMS = ../bin/test\n' +
		 '___bin_test_SOURCES = \n' +
		 '#___bin_test_CXXFLAGS = \n' +
		 'EXTRA_DIST = \n' +
		 '#___bin_test_LDADD = \n'  +
		 '___bin_test_LDFLAGS = -lboost_unit_test_framework')
am.close()
os.system('cp ' + fromwhere + '/*.cpp ../src')
os.chdir('../src')
am = open('Makefile.am', 'w')
am.write('INCLUDES = -I$(top_srcdir)/include\n' +
		 'noinst_PROGRAMS = ../bin/' + project + '\n' +
		 '___bin_' + project + '_SOURCES = main.cc\n' +
		 '#___bin_' + project + '_LDADD = $(top_builddir)/lib/libcommon.a\n'
		 '#EXTRA_DIST = \n' +
		 '#___bin_' + project + '_CXXFLAGS = ')
am.close()
os.chdir('..')
os.system('cp ' + fromwhere + '/*.hpp ../include')

# append files
print('Appending some files...')
os.system('touch NEWS')
os.system('touch README')
os.system('touch AUTHORS')
os.system('touch COPYING')
os.system('touch INSTALL')
os.system('touch ChangeLog')

# configure
print('Configure...')
os.system('aclocal')
os.system('autoheader')
os.system('autoconf')
os.system('automake --add-missing')

# build
print('Building...')
os.chdir('build')
os.system('../configure --enable-debug')
os.system('make')

