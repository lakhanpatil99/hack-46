import re
css = open('uicons.css', encoding='utf-8').read()
targets = ['document', 'chart-pie-alt', 'clipboard-list', 'check-circle', 'settings-sliders', 'marker', 'globe', 'repeat', 'refresh', 'document-signed', 'check-double', 'thumbtack', 'calendar', 'badge-check', 'map-marker', 'chart-histogram', 'list-check']

for t in targets:
    m = re.search(r'\.fi-rr-' + t + r':before\s*\{\s*content:\s*"\\([^"]+)"', css)
    if m:
        print(f"{t}: \\{m.group(1)}")
    else:
        # try without strict braces
        m = re.search(r'\.fi-rr-' + t + r':before.*?content:\s*"\\([^"]+)"', css, re.DOTALL)
        if m:
            print(f"{t}: \\{m.group(1)}")
