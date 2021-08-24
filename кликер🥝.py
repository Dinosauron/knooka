from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
t = True
n = 0
class m(App):
	def build(self):
		f1 = FloatLayout()
		f1.add_widget(Button(
		text = '0',
		font_size = 110,
		background_color = [1,0,0,1],
		background_normal = ' ',
		on_press = self.ccol))
		return f1
	def ccol(self,g):
		global t,n
		if t:
			g.background_color = [0,1,0,1]
			t = False
			n+=1
			g.text = str(n)
		else:
			g.background_color = [1,0,0,1]
			t = True
			n+=1
			g.text = str(n)
if __name__ == '__main__':
	m().run()