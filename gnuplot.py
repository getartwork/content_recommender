from os import system, remove

gnuplot_command = "gnuplot -e \"set term dumb; plot \'{}\' title \'{}\'\""

def windows_gnuplot_command(filename, title):
    system(gnuplot_command.format(filename, title))

def linux_gnuplot_command():
    x11_command_1 = u"set style line 1 lc rgb \'#0060ad\' lt 1 lw 2 pt 7 ps 1.5   # --- blue;"
    x11_command_2 = u"plot \'rank_list.dat\' title \'500 most frequent words occurrences\' with linespoints ls 1"
    f = io.open('tmp_gnuplot.gp', 'w')
    f.write((x11_command_1 + " " + x11_command_2))
    system('gnuplot tmp_gnuplot.gp')
    #remove('tmp_gnuplot.gp')


def X_is_running():
    from subprocess import Popen, PIPE
    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    return p.returncode == 0