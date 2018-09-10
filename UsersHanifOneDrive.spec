# -*- mode: python -*-

block_cipher = None


a = Analysis(['UsersHanifOneDrive', '-', 'Texas', 'Tech', 'UniversityApplicationLearnPython', 'BootcampComplete-Python-3-Bootcamp04-Milestone', 'Project', '-', '1TicTacToe.py'],
             pathex=['C:\\Users\\Hanif\\OneDrive - Texas Tech University\\Application\\Learn\\Python Bootcamp\\Complete-Python-3-Bootcamp'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='UsersHanifOneDrive',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
