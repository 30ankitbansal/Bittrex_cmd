from setuptools import setup


setup(
    name="cmdtool",
    version='0.1',
    py_modules=['cmdtool'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hist_data=cmdtool:hist_data
        pnl=cmdtool:pnl
        update_pf=cmdtool:update_pf
    ''',
)
