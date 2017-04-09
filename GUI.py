from tkinter import *
from tkinter import messagebox
import re
import results
import twitter_preprocessing
import twitter_features_matrix
from numpy import transpose
import classifiers
import grafice

class MyApp(object):
  

	def __init__(self, parent):
		self.root = parent
		self.root.title("ANALIZA DISCURSULUI POLITIC PE RETELE DE SOCIALIZARE")
		self.frame = Frame(parent,bg='Cyan')
		self.root['bg']='Cyan'

		def getGrafic():
			grafice.plotResults(results.countedResultsForHC(),results.countedResultsForBS(),results.countedResultsForDT())

		def predict():
			if len(text.get("1.0",END))==1:
				messagebox.showinfo("Eroare","Introduceti tweet")
			else:
				pattern=re.compile(r'\n')
				lista=[]
				lista.append(text.get("1.0",END))
				final=[]
				for i in lista:
					final.append(re.sub(pattern,'',i))
				text.delete('1.0', END)
				processed=twitter_preprocessing.removePunctuationFromText(final)
				postagged=twitter_preprocessing.POSTAGTwitterData(processed)
				matrix=twitter_features_matrix.twitterFeaturesMatrix(processed,postagged).transpose()
				GBC=classifiers.loadGBC()
				res=GBC.predict(matrix)
				
				if res==0:
					var='False'
				if res==1:
					var='True'

				sep=" "
				seq=(str(final[0]),str("\n\n\tTweetul este: "),str(var))
				raspuns=sep.join(seq)
				messagebox.showinfo("Result",raspuns)


		labelTweet=Label(parent,bg='Cyan',font = "Helvetica 16 bold")
		labelTweet.pack(side=TOP)
		labelTweet.configure(text="Tweet")

		text=Text(bg='Light Cyan')
		text.pack()

		btnAnalizeaza=Button(self.frame,text="Analizeaza",fg='Black', bg='Cyan',font = "Helvetica 13 bold")
		btnAnalizeaza.pack(side=LEFT,padx=20, pady=20)
		btnAnalizeaza.configure(command=predict)

		btnGrafic=Button(self.frame,text="Grafic",fg='Black', bg='Cyan',font = "Helvetica 13 bold")
		btnGrafic.pack(side=LEFT,padx=20, pady=20)
		btnGrafic.configure(command=getGrafic)


		btnStatistici = Button(self.frame, text="Statistici", command=self.openFrame,fg='Black', bg='Cyan',font = "Helvetica 13 bold")
		btnStatistici.pack(side=LEFT,padx=20, pady=20)

		btnExit=Button(self.frame,text="Exit",command=self.Exit,fg='Black', bg='Cyan',font = "Helvetica 13 bold")
		btnExit.pack(side=LEFT,padx=20, pady=20)

		self.frame.pack()

	def hide(self):
		self.root.withdraw()
 

	def openFrame(self):
		# self.hide()
		otherFrame = Toplevel()
		otherFrame.geometry("450x350")
		otherFrame.title("STATISTICI")
		otherFrame['bg']='Cyan'

		handler = lambda: self.onCloseOtherFrame(otherFrame)
	    
		btn = Button(otherFrame, text="Exit", command=handler,fg='Black', bg='Cyan',font = "Helvetica 13 bold")
		btn.pack(side=BOTTOM)

		rezultat1 = results.printStatisticsHC()
		text = Text(otherFrame,bg='Light Cyan',font = "Times 10 bold")
		text.insert(END, rezultat1)
		rezultat1 = results.printStatisticsBS()
		text.insert(END, rezultat1)



		rezultat1 = results.printStatisticsDT()
		text.insert(END, rezultat1)
		text.config(state=DISABLED)
		text.pack()

	def onCloseOtherFrame(self, otherFrame):
		otherFrame.destroy()
		self.show()
 

	def show(self):
		self.root.update()
		self.root.deiconify()
 
	def Exit(self):
		self.root.destroy()

	
if __name__ == "__main__":
    root = Tk()
    root.geometry("640x480")
    app = MyApp(root)
    root.mainloop()





