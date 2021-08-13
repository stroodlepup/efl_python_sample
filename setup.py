#!/usr/bin/env python
# encoding: utf-8

#  python setup.py check
#  python setup.py build
#  python setup.py run
#  python setup.py install
#  python setup.py clean --all


from distutils.core import setup, Command
from distutils.version import StrictVersion
from efl.utils.setup import build_extra, build_edc, build_fdo, build_i18n, uninstall
from efl import __version__ as efl_version


MIN_EFL = '1.18'
if StrictVersion(efl_version) < MIN_EFL:
    print('Your python-efl version is too old! Found: ' + efl_version)
    print('You need at least version ' + MIN_EFL)
    exit(1)


class run_in_tree(Command):
   description = 'Run the main() from the build folder (without install)'
   user_options = []

   def initialize_options(self):
      pass

   def finalize_options(self):
      pass

   def run(self):
        import sys, platform

        sys.path.insert(0, 'build/lib.%s-%s-%d.%d' % (
            platform.system().lower(), platform.machine(),
            sys.version_info[0], sys.version_info[1]))

        from efl_python_sample.main import main
        sys.exit(main())


setup(
    name = 'efl_python_sample',
    version = '0.0.1',
    description = 'Short description',
    long_description = 'A longer description of your project',
    author = 'Donn Atienza',
    author_email = 'stroodlepup@gmail.com',
    url = '',
    license = "3-Clause BSD",
    package_dir = {'efl_python_sample': 'src'},
    packages = ['efl_python_sample'],
    requires = ['efl'],
    scripts = ['bin/efl_python_sample'],
    cmdclass = {
        'build': build_extra,
        'build_fdo': build_fdo,
        # 'build_edc': build_edc,
        # 'build_i18n': build_i18n,
        'run': run_in_tree,
        'uninstall': uninstall,
    },
    command_options = {
        'install': {'record': ('setup.py', 'installed_files.txt')}
    },
)

