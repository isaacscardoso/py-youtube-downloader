# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[('/home/mobley/.local/lib/python3.12/site-packages/yt_dlp', 'yt_dlp')],
    datas=[],
    hiddenimports=[
        'yt_dlp',
        'getpass',
        'optparse',
        'xml',
        'xml.etree',
        'xml.etree.ElementTree',
        'glob',
        'http.cookies',
        'json',
        'hmac',
        'html',
        'html.parser',
        'platform',
        'shlex',
        'concurrent',
        'concurrent.futures',
        '__future__',
        'uuid',
        'asyncio',
        'fileinput'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
