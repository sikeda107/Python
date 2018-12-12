filename = input('type file name > ')
# filename = 'array.txt'
print('file name is ' + filename)
output = './tex_'+filename
with open(output, mode='w') as fp_out:
    fp_out.write('\\begin{equation}\n')
    fp_out.write(input('array name >'))
    fp_out.write(' = \n')
    fp_out.write('\\begin{pmatrix}\n')
    with open(filename) as fp:
        for line in fp:
            line_s = '&'.join(line.split())
            print(list(line_s))
            fp_out.write(line_s + '\\\\\n')

    fp_out.write('\\end{pmatrix}\n')
    fp_out.write('\\label{eq:matrix}\n')
    fp_out.write('\\end{equation}\n')

print('END')
