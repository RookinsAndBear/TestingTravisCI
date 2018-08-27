''' ExtractEphemData.py
    Extract data from STK(ODTK) generated ephermeris files.

    INPUT:  ephemeris file name (example.e found in adam_home/data/ephem)
            reference time for analysis (from epoch in seconds)

    OUTPUT: values_stk:     STK data matrix [28 x 1]:
                            7 x 1  time, position, velocity
                            21 x 1 state covariance matrix lower
                                    triangular format

METHOD LIST:    odtk_ExtractPosVelCov
                dummy_ExtractPosVelCov

'''


def odtk_ExtractPosVelCov(ephemFile, ref_time):
    ''' odtk_ExtractPosVelCov:  Search ephemeris file for reference time and
                                 extract Time, Pos, Vel, Lower Tri Cov Matrix

        INPUT:  ephemFile:      string path and file name
                ref_time:       integer reference time to search for (sec)

        OUTPUT: values_stk:     STK data matrix [28 x 1]:
                                7 x 1  time, position, velocity
                                21 x 1 state covariance matrix lower
                                        triangular format
    '''

    try:
        open(ephemFile, 'r')
    except(FileNotFoundError):
        print("File Name or File Path Not Found")

    if ref_time.find('e') > 0 or ref_time.find('E') > 0:
        raise ValueError('Reference time can not be in scientific notation')

    f = open(ephemFile, 'r')
    lines = f.readlines()
    count = 0
    linenum = 0
    convertTime = 0

    for x in lines:
        linenum = linenum + 1
        if x.split(' ')[0].find("e+") == -1:
            pass
        else:
            convertTime = str(int(float("{:.8f}".
                          format(float(x.split(' ')[0])))))

        if convertTime == ref_time and len(x.split(' ')) > 1:
            count = count + 1
            if count == 1:
                TimePosVel = x.split(' ')
            if count == 2:
                Cov_1 = x.split(' ')
                Cov_2 = lines[linenum].split(' ')
                Cov_2 = Cov_2[22:len(Cov_2)]
                Cov_3 = lines[linenum+1].split(' ')
                Cov_3 = Cov_3[22:len(Cov_3)]

    f.close()
    values_stk = [TimePosVel[0], TimePosVel[1], TimePosVel[2], TimePosVel[3],
                  TimePosVel[4], TimePosVel[5], TimePosVel[6],
                  Cov_1[1], Cov_1[2], Cov_1[3],
                  Cov_1[4], Cov_1[5], Cov_1[6], Cov_1[7],
                  Cov_2[0], Cov_2[1], Cov_2[2],
                  Cov_2[3], Cov_2[4], Cov_2[5], Cov_2[6],
                  Cov_3[0], Cov_3[1], Cov_3[2],
                  Cov_3[3], Cov_3[4], Cov_3[5], Cov_3[6]]

    return values_stk


def dummy_ExtractPosVelCov(ephemFile, ref_time):
    ''' dummy_ExtractPosVelCov: demo STK visualiztion ipynb STK .e file format
                                 - testing purposes
                                original file does not contain covariance
                                 matrix.
                                Search ephemeris file for reference time and 
                                 extract Time, Pos, Vel, Lower Tri Cov Matrix.

        INPUT:  ephemFile:      string path and file name
                ref_time:       integer reference time to search for (sec)

        OUTPUT: values_stk:     STK data matrix [28 x 1]:
                                7 x 1  time, position, velocity
                                21 x 1 state covariance matrix lower 
                                        triangular format
    '''

    try:
        with open(ephemFile, 'r') as f:
            f.close()
    except(FileNotFoundError):
        print("File Name or File Path Not Found")

    if ref_time.find('e') > 0 or ref_time.find('E') > 0:
        raise ValueError('Reference time can not be in scientific notation')

    # read ephem file
    lines = []
    with open(ephemFile, 'r') as f:
        for line in f:
            lines.append(line)
        for linenum, line in enumerate(lines):
            str = lines[linenum]
            if str.find(ref_time) == 0:
                # dummy ephem file uses tabs from importing into Excel
                values_stk = str.split('\t') 
                #values = str.split(' ') # real ephem files use spaces
    f.close()

    return values_stk

