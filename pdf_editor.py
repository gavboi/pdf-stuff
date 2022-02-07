from PyPDF2 import PdfFileMerger
from os import path

location = ''
def getLocation():
    global location
    location = ''
    while location == '':
        location = input('Input new directory: ').strip()
        if not path.isdir(location):
            print('"' + location + '" is not a valid directory.')
            location = ''
    print()

def funcMerge():
    # get file names
    valid = False
    while not valid:
        conf = 'temp'
        while conf != 'y':
            # input desired files
            base = input('\nInput filename base: ')
            suffix = input('Input filename page suffix: ')
            count = int(input('Input page files count: '))
            conf = input('\nIs this format ok? "' + base +
                         suffix.replace('#', str(count)) +
                         '.pdf"\n[y]/[n] : ').strip()
            if conf == 'y' and path.isfile(
                path.join(location, base + '.pdf')):
                    conf = input(base + '.pdf" exists. Overwrite?' +
                                 '\n[y]/[n] : ').strip()
        # check they exist
        print()
        valid = True
        queue = []
        for i in range(1, count + 1):
            file = base + suffix.replace('#', str(i)) + '.pdf'
            if path.isfile(path.join(location, file)):
                print('"' + file + '" found.')
                queue.append(file)
            else:
                print('"' + file + '" does not exist ' +
                        'in the current directory.')
                valid = False
        if not valid:
            print('Could not find all specified files.\n')
    # make new file
    merger = PdfFileMerger()
    for file in queue:
        merger.append(path.join(location, file))
    merger.write(open(path.join(location, base + '.pdf'), mode = 'wb'))
    if path.isfile(path.join(location, base + '.pdf')):
        print('\n"' + base + '.pdf" created.\n')
    else:
        print('\nSomething went wrong! File was not created.\n')
        
inp = 'temp'
while inp != '':
    if location == '' or inp == 'd':
        getLocation()
    if inp == 'm':
        funcMerge()
    inp = input('Current directory - ' + location +
                '\nSelect function - [d]irectory [m]erge : '
                ).strip()

print('Done!')
