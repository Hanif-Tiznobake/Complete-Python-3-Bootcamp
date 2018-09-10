# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Hanif\\OneDrive - Texas Tech University\\Application\\Learn\\Python Bootcamp\\Complete-Python-3-Bootcamp\\04-Milestone Project - 1\\TicTacToe.py'],
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
          name='TicTacToe',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
