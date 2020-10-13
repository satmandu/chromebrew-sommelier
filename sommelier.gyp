{
  'targets': [
    {
      'target_name': 'sommelier-protocol',
      'type': 'static_library',
      'variables': {
        'wayland_in_dir': '.',
        'wayland_out_dir': '.',
      },
      'sources': [
        'aura-shell.xml',
        'drm.xml',
        'gtk-shell.xml',
        'keyboard-extension-unstable-v1.xml',
        'linux-dmabuf-unstable-v1.xml',
        'viewporter.xml',
        'xdg-shell-unstable-v6.xml',
      ],
      'includes': ['wayland-protocol.gypi'],
    },
    {
      'target_name': 'sommelier',
      'type': 'executable',
      'variables': {
        'exported_deps': [
          'gbm',
          'pixman-1',
          'wayland-client',
          'wayland-server',
          'xcb',
          'xcb-composite',
          'xcb-xfixes',
          'xkbcommon',
        ],
        'pkg-config': ['pkg-config'],
        'deps': ['<@(exported_deps)'],
      },
      'link_settings': {
        'libraries': [
          '<!@(<(pkg-config) --libs-only-l <(deps))',
          '-lm',
        ],
        'ldflags': [
          '<!@(<(pkg-config) --libs-only-L --libs-only-other <(deps))',
        ],
      },
      'dependencies': [
        'sommelier-protocol',
      ],
      'sources': [
        'sommelier.c',
      ],
      'defines': [
        '_GNU_SOURCE',
        'WL_HIDE_DEPRECATED',
        'XWAYLAND_PATH="/usr/bin/Xwayland"',
      ],
      'cflags': [
        '<!@(<(pkg-config) --cflags <(deps))',
      ]
    },
  ],
}
