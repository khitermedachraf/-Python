
import sys
mark1 = sys.argv[1]
mark2 = sys.argv[2]
mark3 =sys.argv[3]
course1 = sys.argv[4]
course2 = sys.argv[5]
course3 = sys.argv[6]
print("Cours1\t"+course1+" = note1\t"+mark1+"\n")
print("Cours2\t"+course2+" = note2\t"+mark2+"\n")
print("Cours3\t"+course3+" = note3\t"+mark3+"\n")
print("-----------------\n")
resultat=int(mark1) + int(mark2) + int(mark3)
resultat=resultat/3
print("moyenne\t="+str(resultat))


