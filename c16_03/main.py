note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

notes_eleve1 = [note1[2], note2[2], note3[2], note4[2], note5[2], note6[2]]

#4a
somme_1 = sum(notes_eleve1)
moy_eleve1 = somme_1/len(notes_eleve1)
print("Moyenne de l'élève 1 :", moy_eleve1)

#4/b
def moyenne_tuples(notes,eleve,matiere):
  s=0
  i = 0
  for x in notes:
    if x[0] == eleve and x[1]== matiere:
      s= s+x[2]
      i = i +1
  moy = s / i
  return moy

print(moyenne_tuples(notes,'eleve1','math'))

#4c

def moyenne():
    somme = 0
    moyenne = 0
    eleve = input("Entrez le nom de l'élève: ")
    matiere  = input("Choisissez la matière: ")
    for i in range(8):
        if(notes[i][0] == eleve):
            if(notes[i][1] == matiere):
                moyenne += notes[i][2]
                somme += 1
    moyenne = moyenne/somme
    print(moyenne)
               
moyenne()

#5
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
   
    def afficherNote(self):
        print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)
       
onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)