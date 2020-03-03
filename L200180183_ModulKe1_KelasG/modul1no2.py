def gambarPersegiEmpat(tinggi,lebar):
    for i in range(0,tinggi):
        if i > 0 and i < tinggi-1:
            for j in range (0,lebar):
                if j > 0 and j < lebar-1:
                    print (' ', end='')
                else:
                    print ('@', end='')
        else:
            for j in range(0,lebar):
                print ('@', end='')
        print ('')
