from kivy import Config
Config.set('graphics', 'minimum_width', '800')
Config.set('graphics', 'minimum_height', '600')


from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import HoverBehavior, MagicBehavior
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDFillRoundFlatButton

from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock

from functools import partial
import os
import shutil
import time
import datetime
import threading

class BuildMainScreen():

    def load(self):
        self.organize=Organize()
        self.quick_organize=QuickOrganize()
        self.quick_organize.bind(on_press= partial(QuickOrganizeScreen.load_animation, self))
        self.tools=Tools()
        self.settings_button=SettingsButton()
        Mainscreenvar = sm.get_screen('MainScreen')
        Mainscreenvar.ids.container.add_widget(self.organize)
        Mainscreenvar.ids.container.add_widget(self.quick_organize)
        Mainscreenvar.ids.container.add_widget(self.tools)
        Mainscreenvar.ids.container.add_widget(self.settings_button)
        anim1=Animation(pos_hint={'center_x':.2, 'center_y':.5}, duration=.3, t='in_out_back')
        anim2=Animation(pos_hint={'center_x':.8, 'center_y':.5}, duration=.3, t='in_out_back')
        anim1.start(self.organize)
        anim2.start(self.tools)

class Organize(MDCard, HoverBehavior):

    def on_enter(self,*args):
        if expandable==True:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.7}, user_font_size=70, duration=.2)
            anim2=Animation(size_hint=(.22,.47), elevation=14, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.3}, font_size=23, color=(0.0039,0.596,0.4588,1),duration=.2)
            anim1.start(self.ids.organize)
            anim2.start(self)
            anim3.start(self.ids.label)

    def on_leave(self,*args):
        if expandable==True:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.5}, user_font_size=90, duration=.2)
            anim2=Animation(size_hint=(.2,.45), elevation=12, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.15}, font_size=15, color=(0,0,0,1), duration=.2)
            anim1.start(self.ids.organize)
            anim2.start(self)
            anim3.start(self.ids.label)

class QuickOrganize(MDCard, HoverBehavior):

    def on_enter(self,*args):
        if expandable==True:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.7}, user_font_size=70, duration=.2)
            anim2=Animation(size_hint=(.22,.47), elevation=14, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.3}, font_size=23, color=(0.0039,0.596,0.4588,1),duration=.2)
            anim1.start(self.ids.quickorganize)
            anim2.start(self)
            anim3.start(self.ids.label)

    def on_leave(self,*args):
        if expandable==True:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.5}, user_font_size=90, duration=.2)
            anim2=Animation(size_hint=(.2,.45), elevation=12, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.15}, font_size=15, color=(0,0,0,1), duration=.2)
            anim1.start(self.ids.quickorganize)
            anim2.start(self)
            anim3.start(self.ids.label)

class Tools(MDCard, HoverBehavior):

    def on_enter(self,*args):
        if expandable==True:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.7}, user_font_size=70, duration=.2)
            anim2=Animation(size_hint=(.22,.47), elevation=14, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.3}, font_size=23, color=(0.0039,0.596,0.4588,1),duration=.2)
            anim1.start(self.ids.tools)
            anim2.start(self)
            anim3.start(self.ids.label)

    def on_leave(self,*args):
        if expandable==True:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.5}, user_font_size=90, duration=.2)
            anim2=Animation(size_hint=(.2,.45), elevation=12, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.15}, font_size=15, color=(0,0,0,1), duration=.2)
            anim1.start(self.ids.tools)
            anim2.start(self)
            anim3.start(self.ids.label)

class SettingsButton(MDFloatingActionButton, MagicBehavior):
    pass


class QuickOrganizeScreen():

    def load_animation(self, instance):
        global expandable
        if expandable == True:
            Mainscreenvar = sm.get_screen('MainScreen')
            anim1=Animation(pos_hint={'center_x':.5, "center_y":.5}, size_hint=(0.9,0.9),duration=.3, t='in_out_back')
            anim1.bind(on_complete=partial(QuickOrganizeScreen.load_ui,self))
            anim2=Animation(size_hint=(0,0), duration=.3, t='in_out_back')
            expandable=False
            anim1.start(instance)
            anim2.start(instance.parent.children[1])
            instance.clear_widgets()
            anim2.start(instance.parent.children[3])
            instance.parent.remove_widget(instance.parent.children[1])


    def load_ui(self, animation_object, instance): # Here self is the card element for quick sort

        instance.parent.remove_widget(instance.parent.children[0])
        instance.parent.remove_widget(instance.parent.children[1])
        self.back_button =MDIconButton(icon='arrow-left',
                                       pos_hint={'top':.98},
                                       user_font_size='30sp'
                                        )
        self.back_button.bind(on_press=partial(QuickOrganizeScreen.back,self))
        instance.add_widget(self.back_button)

        self.desktop=Desktop()
        self.desktop.bind(on_press=partial(QuickOrganizeScreen.selector, self))
        self.downloads=Downloads()
        self.downloads.bind(on_press=partial(QuickOrganizeScreen.selector, self))
        self.documents=Documents()
        self.documents.bind(on_press=partial(QuickOrganizeScreen.selector, self))
        self.layout_holder = RelativeLayout(size=instance.size,
                                       pos=instance.pos)
        self.heading_label = Label(text="Select what folders you want to quick sort",
                                   pos_hint={'center_x':.45, 'center_y':.85},
                                   color=(0,0,0,1),
                                   font_name='Roboto-Medium',
                                   font_size='26sp'
                                   )
        self.quick_organize_start_button= MDFillRoundFlatButton(text='start',
                                                         pos_hint={'center_x':.45, 'center_y':.15},
                                                         )
        self.quick_organize_start_button.bind(on_press=partial(QuickOrganizeScreen.quick_organize_desktop,self))
        self.layout_holder.add_widget(self.heading_label)
        self.layout_holder.add_widget(self.desktop)
        self.layout_holder.add_widget(self.downloads)
        self.layout_holder.add_widget(self.documents)
        self.layout_holder.add_widget(self.quick_organize_start_button)
        self.removed = False
        instance.add_widget(self.layout_holder)


    def selector(self, instance):
        global selected
        value=list(instance.ids.keys())[0]
        if value in selected:
            selected.remove(value)

        else:
            selected.append(value)
    def back(self, instance):
        Mainscreenvar = sm.get_screen('MainScreen')
        global expandable, selected
        expandable = True
        selected=[]
        instance.parent.clear_widgets()
        anim1=Animation(size_hint=(0.2,0.45),duration=.3, t='in_out_back')
        anim1.bind(on_complete=partial(QuickOrganizeScreen.remover, self))
        anim1.start(Mainscreenvar.ids.container.children[0])

    def remover(self, *args):
        Mainscreenvar = sm.get_screen('MainScreen')
        Mainscreenvar.ids.container.clear_widgets()
        BuildMainScreen.load(self)

    def screen_clearer(self, instance, *args):
        instance.parent.parent.remove_widget(instance.parent.parent.children[1])
        instance.parent.clear_widgets()

    def dektop_loaded_updater(self,*args):
        Mainscreenvar = sm.get_screen('MainScreen')
        if self.desktop_sorted == False:
            self.update = Label(text= 'Now sorting your Desktop',
                                pos_hint={'center_x':.45,"center_y":.5},
                                color = (0,0,0,1),
                                font_name = 'Roboto-Bold',
                                font_size = '20sp',
                                opacity = 0)
            Mainscreenvar.ids.container.children[0].children[0].opacity = 1
            Mainscreenvar.ids.container.children[0].children[0].add_widget(self.update)
            anim1 = Animation(opacity = 1, duration = .3)
            anim1.start(self.update)

    def downloads_loaded_updater(self,*args):
        Mainscreenvar = sm.get_screen('MainScreen')
        if self.downloads_sorted == False:
            self.update = Label(text= 'Now sorting your Desktop',
                                pos_hint={'center_x':.45,"center_y":.5},
                                color = (0,0,0,1),
                                font_name = 'Roboto-Bold',
                                font_size = '20sp',
                                opacity = 0)
            Mainscreenvar.ids.container.children[0].children[0].opacity = 1
            Mainscreenvar.ids.container.children[0].children[0].add_widget(self.update)
            anim1 = Animation(opacity = 1, duration = .3)
            anim1.start(self.update)

    def documents_loaded_updater(self,*args):
        Mainscreenvar = sm.get_screen('MainScreen')
        if self.documents_sorted == False:
            self.update = Label(text= 'Now sorting your Desktop',
                                pos_hint={'center_x':.45,"center_y":.5},
                                color = (0,0,0,1),
                                font_name = 'Roboto-Bold',
                                font_size = '20sp',
                                opacity = 0)
            Mainscreenvar.ids.container.children[0].children[0].opacity = 1
            Mainscreenvar.ids.container.children[0].children[0].add_widget(self.update)
            anim1 = Animation(opacity = 1, duration = .3)
            anim1.start(self.update)




    def quick_organize_desktop(self, instance,*args):
        if 'desktop' in selected:
            if self.removed == False:
                anim1 = Animation(opacity = 0, duration = .3)
                anim1.bind(on_complete = partial(QuickOrganizeScreen.screen_clearer,self,instance))
                anim1.start(instance.parent)
            files=[]
            self.desktop_sorted = False
            Clock.schedule_once(partial(QuickOrganizeScreen.dektop_loaded_updater, self), .2)
            self.desktop_sorted = False
            path='/home/guhan/Desktop'
            for i in os.listdir(path):
                full_path=os.path.join(path, i)
                if os.path.isfile(full_path):
                    files.append(full_path)
            for j in files:
                ext = os.path.splitext(j)[1]

                if ext in pictures_format:
                    if os.path.isdir(path + '/Images'):
                        shutil.move(j, path +'/Images')
                    else:
                        os.mkdir(path +'/Images')
                        shutil.move(j, path+'/Images')

                elif ext in video_format:
                    if os.path.isdir(path +'/Videos'):
                        shutil.move(j, path +'/Videos')
                    else:
                        os.mkdir(path +'/Videos')
                        shutil.move(j, path +'/Videos')

                elif ext in documents_format:
                    if os.path.isdir(path +'/Documents'):
                        shutil.move(j, path +'/Documents')
                    else:
                        os.mkdir(path +'/Documents')
                        shutil.move(j, path +'/Documents')

                elif ext in zipped_format:
                    if os.path.isdir(path +'/Zipped files'):
                        shutil.move(j, path +'/Zipped files')
                    else:
                        os.mkdir(path +'/Zipped files')
                        shutil.move(j, path +'/Zipped files')

                elif ext in audio_format:
                    if os.path.isdir(path +'/audio'):
                        shutil.move(j, path +'/audio')
                    else:
                        os.mkdir(path +'/audio')
                        shutil.move(j, path +'/audio')

                else:
                    pass

            if os.path.isdir(path + '/Documents'):
                documents_folder_path = path +'/Documents'
                documents = os.listdir(documents_folder_path)
                for g in documents:
                    file_path = documents_folder_path + '/' + g
                    ext = os.path.splitext(g)[-1]

                    if ext in ['.docx','.docm','.dotx','.dotm','.docb','.doc']:
                        if os.path.isdir(documents_folder_path +'/Word Documents'):
                            shutil.move(file_path, documents_folder_path +'/Word Documents')
                        else:
                            os.mkdir(documents_folder_path +'/Word Documents')
                            shutil.move(file_path, documents_folder_path +'/Word Documents')

                    elif ext == '.pdf':
                        if os.path.isdir(documents_folder_path + "/PDF"):
                            shutil.move(file_path, documents_folder_path + "/PDF")
                        else:
                            os.mkdir(documents_folder_path + "/PDF")
                            shutil.move(file_path, documents_folder_path +"/PDF")

                    elif ext == '.txt':
                        if os.path.isdir(documents_folder_path + '/Text Files'):
                            shutil.move(file_path, documents_folder_path + '/Text Files')
                        else:
                            os.mkdir(documents_folder_path + '/Text Files')
                            shutil.move(file_path, documents_folder_path +'/Text Files')

                    elif ext in ['.xls','.xlt','.xlm','.xlsx','xlsm','xltx','xltm']:
                        if os.path.isdir(documents_folder_path + '/Excel Documents'):
                            shutil.move(file_path, documents_folder_path + '/Excel Documents')
                        else:
                            os.mkdir(documents_folder_path + '/Excel Documents')
                            shutil.move(file_path, documents_folder_path +'/Excel Documents')

                    elif ext in ['.ppt','.pptx','.pot','.pps','.pptm','.potx','.potm','.ppsx','.ppsm','.sldx','.sldm']:
                        if os.path.isdir(documents_folder_path + '/Powerpoints'):
                            shutil.move(file_path, documents_folder_path + '/Powerpoints')
                        else:
                            os.mkdir(documents_folder_path + '/Powerpoints')
                            shutil.move(file_path, documents_folder_path +'/Powerpoints')

                    else:
                        pass

            # The code for second level of sorting...ie date sorting
            if os.path.isdir(path +'/Images'): # This is the sorting for images
                image_folder_path= path+ '/Images'
                images = os.listdir(image_folder_path)
                list = []
                for p in images:
                    date = os.path.getctime(image_folder_path + '/' + p)
                    date = time.strftime('%Y-%m-%d', time.localtime(date))
                    list.append((image_folder_path + '/' + p, date))
                sorted_list = sorted(list, key=lambda x:x[::-1])
                for a in sorted_list:
                    folder_name = datetime.datetime.strptime(a[1], '%Y-%m-%d').strftime('%b %Y')
                    folder_path = path + '/Images' + '/' + folder_name
                    if os.path.isdir(folder_path):
                        shutil.move(a[0], folder_path)
                    else:
                        os.mkdir(folder_path)
                        shutil.move(a[0], folder_path)

            if os.path.isdir(path + '/Videos'): # This is for sorting videos based on dates
                video_folder_path = path + '/Videos'
                videos = os.listdir(video_folder_path)
                list = []
                for v in videos:
                    date = os.path.getctime(video_folder_path + '/' + v)
                    date = time.strftime('%Y-%m-%d', time.localtime(date))
                    list.append((video_folder_path + '/' + v, date))
                sorted_list = sorted(list, key=lambda x:x[::-1])
                for i in sorted_list:
                    folder_name = datetime.datetime.strptime(i[1], '%Y-%m-%d').strftime('%b %Y')
                    folder_path = path + '/Videos' + '/' + folder_name
                    if os.path.isdir(folder_path):
                        shutil.move(i[0], folder_path)
                    else:
                        os.mkdir(folder_path)
                        shutil.move(i[0], folder_path)

            self.removed = True
            self.desktop_sorted = True
            QuickOrganizeScreen.dektop_loaded_updater(self)
            QuickOrganizeScreen.quick_organize_downloads(self, instance)
        else:
            self.desktop_sorted = True
            QuickOrganizeScreen.quick_organize_downloads(self, instance)



    def quick_organize_downloads(self, instance):
        if 'downloads' in selected:
            if self.removed == False:
                anim1 = Animation(opacity = 0, duration = .3)
                anim1.bind(on_complete = partial(QuickOrganizeScreen.screen_clearer,self,instance))
                anim1.start(instance.parent)
            self.downloads_sorted = False
            Clock.schedule_once(partial(QuickOrganizeScreen.downloads_loaded_updater,self),.2)
            files=[]
            path='/home/guhan/Downloads'
            for i in os.listdir(path):
                full_path=os.path.join(path, i)
                if os.path.isfile(full_path):
                    files.append(full_path)

            for j in files:
                ext = os.path.splitext(j)[1]

                if ext in pictures_format:
                    if os.path.isdir(path + '/Images'):
                        shutil.move(j, path +'/Images')
                    else:
                        os.mkdir(path +'/Images')
                        shutil.move(j, path+'/Images')

                elif ext in video_format:
                    if os.path.isdir(path +'/Videos'):
                        shutil.move(j, path +'/Videos')
                    else:
                        os.mkdir(path +'/Videos')
                        shutil.move(j, path +'/Videos')

                elif ext in documents_format:
                    if os.path.isdir(path +'/Documents'):
                        shutil.move(j, path +'/Documents')
                    else:
                        os.mkdir(path +'/Documents')
                        shutil.move(j, path +'/Documents')

                elif ext in zipped_format:
                    if os.path.isdir(path +'/Zipped files'):
                        shutil.move(j, path +'/Zipped files')
                    else:
                        os.mkdir(path +'/Zipped files')
                        shutil.move(j, path +'/Zipped files')

                elif ext in audio_format:
                    if os.path.isdir(path +'/audio'):
                        shutil.move(j, path +'/audio')
                    else:
                        os.mkdir(path +'/audio')
                        shutil.move(j, path +'/audio')

                elif ext in installer_format:
                    if os.path.isdir(path +'/installers'):
                        shutil.move(j, path +'/installers')
                    else:
                        os.mkdir(path +'/installers')
                        shutil.move(j, path +'/installers')
                else:
                    if os.path.isdir(path +'/other'):
                        shutil.move(j, path +'/other')
                    else:
                        os.mkdir(path +'/other')
                        shutil.move(j, path +'/other')

            if os.path.isdir(path + '/Documents'):
                documents_folder_path = path +'/Documents'
                documents = os.listdir(documents_folder_path)
                for g in documents:
                    file_path = documents_folder_path + '/' + g
                    ext = os.path.splitext(g)[-1]

                    if ext in ['.docx','.docm','.dotx','.dotm','.docb','.doc']:
                        if os.path.isdir(documents_folder_path +'/Word Documents'):
                            shutil.move(file_path, documents_folder_path +'/Word Documents')
                        else:
                            os.mkdir(documents_folder_path +'/Word Documents')
                            shutil.move(file_path, documents_folder_path +'/Word Documents')

                    elif ext == '.pdf':
                        if os.path.isdir(documents_folder_path + "/PDF"):
                            shutil.move(file_path, documents_folder_path + "/PDF")
                        else:
                            os.mkdir(documents_folder_path + "/PDF")
                            shutil.move(file_path, documents_folder_path +"/PDF")

                    elif ext == '.txt':
                        if os.path.isdir(documents_folder_path + '/Text Files'):
                            shutil.move(file_path, documents_folder_path + '/Text Files')
                        else:
                            os.mkdir(documents_folder_path + '/Text Files')
                            shutil.move(file_path, documents_folder_path +'/Text Files')

                    elif ext in ['.xls','.xlt','.xlm','.xlsx','xlsm','xltx','xltm']:
                        if os.path.isdir(documents_folder_path + '/Excel Documents'):
                            shutil.move(file_path, documents_folder_path + '/Excel Documents')
                        else:
                            os.mkdir(documents_folder_path + '/Excel Documents')
                            shutil.move(file_path, documents_folder_path +'/Excel Documents')

                    elif ext in ['.ppt','.pptx','.pot','.pps','.pptm','.potx','.potm','.ppsx','.ppsm','.sldx','.sldm']:
                        if os.path.isdir(documents_folder_path + '/Powerpoints'):
                            shutil.move(file_path, documents_folder_path + '/Powerpoints')
                        else:
                            os.mkdir(documents_folder_path + '/Powerpoints')
                            shutil.move(file_path, documents_folder_path +'/Powerpoints')

                    else:
                        pass



            # The code for second level of sorting...ie date sorting
            if os.path.isdir(path +'/Images'): # This is the sorting for images
                image_folder_path= path+ '/Images'
                images = os.listdir(image_folder_path)
                list = []
                for p in images:
                    date = os.path.getctime(image_folder_path + '/' + p)
                    date = time.strftime('%Y-%m-%d', time.localtime(date))
                    list.append((image_folder_path + '/' + p, date))
                sorted_list = sorted(list, key=lambda x:x[::-1])
                for a in sorted_list:
                    folder_name = datetime.datetime.strptime(a[1], '%Y-%m-%d').strftime('%b %Y')
                    folder_path = path + '/Images' + '/' + folder_name
                    if os.path.isdir(folder_path):
                        shutil.move(a[0], folder_path)
                    else:
                        os.mkdir(folder_path)
                        shutil.move(a[0], folder_path)

            if os.path.isdir(path + '/Videos'): # This is for sorting videos based on dates
                video_folder_path = path + '/Videos'
                videos = os.listdir(video_folder_path)
                list = []
                for v in videos:
                    date = os.path.getctime(video_folder_path + '/' + v)
                    date = time.strftime('%Y-%m-%d', time.localtime(date))
                    list.append((video_folder_path + '/' + v, date))
                sorted_list = sorted(list, key=lambda x:x[::-1])
                for i in sorted_list:
                    folder_name = datetime.datetime.strptime(i[1], '%Y-%m-%d').strftime('%b %Y')
                    folder_path = path + '/Videos' + '/' + folder_name
                    if os.path.isdir(folder_path):
                        shutil.move(i[0], folder_path)
                    else:
                        os.mkdir(folder_path)
                        shutil.move(i[0], folder_path)

            self.removed = True
            self.downloads_sorted = True
            QuickOrganizeScreen.downloads_loaded_updater(self)
            QuickOrganizeScreen.quick_organize_documents(self, instance)
        else:
            self.downloads_sorted = True
            QuickOrganizeScreen.downloads_loaded_updater(self)
            QuickOrganizeScreen.quick_organize_documents(self, instance)

    def quick_organize_documents(self, instance):
        if 'documents' in selected:
            if self.removed == False:
                anim1 = Animation(opacity = 0, duration = .3)
                anim1.bind(on_complete = partial(QuickOrganizeScreen.screen_clearer,self,instance))
                anim1.start(instance.parent)
            self.documents_sorted = False
            Clock.schedule_once(partial(QuickOrganizeScreen.documents_loaded_updater,self),.2)
            files=[]
            path='/home/guhan/Documents'
            for i in os.listdir(path):
                full_path=os.path.join(path, i)
                if os.path.isfile(full_path):
                    files.append(full_path)
            for j in files:
                ext = os.path.splitext(j)[1]

                if ext in documents_format:
                    if os.path.isdir(path +'/Documents'):
                        shutil.move(j, path +'/Documents')
                    else:
                        os.mkdir(path +'/Documents')
                        shutil.move(j, path +'/Documents')

                elif ext in zipped_format:
                    if os.path.isdir(path +'/Zipped files'):
                        shutil.move(j, path +'/Zipped files')
                    else:
                        os.mkdir(path +'/Zipped files')
                        shutil.move(j, path +'/Zipped files')

                else:
                    pass

            if os.path.isdir(path):
                documents_folder_path = path
                documents = os.listdir(documents_folder_path)
                for g in documents:
                    file_path = documents_folder_path + '/' + g
                    ext = os.path.splitext(g)[-1]

                    if ext in ['.docx','.docm','.dotx','.dotm','.docb','.doc']:
                        if os.path.isdir(documents_folder_path +'/Word Documents'):
                            shutil.move(file_path, documents_folder_path +'/Word Documents')
                        else:
                            os.mkdir(documents_folder_path +'/Word Documents')
                            shutil.move(file_path, documents_folder_path +'/Word Documents')

                    elif ext == '.pdf':
                        if os.path.isdir(documents_folder_path + "/PDF"):
                            shutil.move(file_path, documents_folder_path + "/PDF")
                        else:
                            os.mkdir(file_path, documents_folder_path + "/PDF")
                            shutil.move(file_path, documents_folder_path +"/PDF")

                    elif ext == '.txt':
                        if os.path.isdir(documents_folder_path + '/Text Files'):
                            shutil.move(file_path, documents_folder_path + '/Text Files')
                        else:
                            os.mkdir(documents_folder_path + '/Text Files')
                            shutil.move(file_path, documents_folder_path +'/Text Files')

                    elif ext in ['.xls','.xlt','.xlm','.xlsx','xlsm','xltx','xltm']:
                        if os.path.isdir(documents_folder_path + '/Excel Documents'):
                            shutil.move(file_path, documents_folder_path + '/Excel Documents')
                        else:
                            os.mkdir(documents_folder_path + '/Excel Documents')
                            shutil.move(file_path, documents_folder_path +'/Excel Documents')

                    elif ext in ['.ppt','.pptx','.pot','.pps','.pptm','.potx','.potm','.ppsx','.ppsm','.sldx','.sldm']:
                        if os.path.isdir(documents_folder_path + '/Powerpoints'):
                            shutil.move(file_path, documents_folder_path + '/Powerpoints')
                        else:
                            os.mkdir(documents_folder_path + '/Powerpoints')
                            shutil.move(file_path, documents_folder_path +'/Powerpoints')

        self.documents_sorted = True
        QuickOrganizeScreen.documents_loaded_updater(self)
        Clock.schedule_once(partial(QuickOrganizeScreen.final_screen,self),.5)


    def final_screen(self, *args):
        Mainscreenvar = sm.get_screen('MainScreen')
        title1 = Label(text="All your files have been sorted succesfully",
                       pos_hint = {'center_x':.5,'center_y':.7},
                       color = (0,0,0,1),
                       font_name = 'Roboto-Bold',
                       opacity = 0,
                       font_size = '25sp')
        Mainscreenvar.ids.container.children[0].children[0].opacity = 1
        Mainscreenvar.ids.container.children[0].children[0].add_widget(title1)
        anim1 = Animation(opacity = 1,pos_hint = {'center_x':.5,'center_y':.8}, duration = .3)
        anim1.start(title1)




class Desktop(MDCard, HoverBehavior):

    def on_enter(self,*args):
        anim1=Animation(pos_hint={'center_x':.5, 'center_y':.65}, duration=.2)
        anim2=Animation(size_hint=(.22,.42), elevation=14, duration=.2)
        anim3=Animation(pos_hint={'center_x':.5, 'center_y':.3}, font_size=23,duration=.2)
        anim1.start(self.ids.desktop)
        anim2.start(self)
        anim3.start(self.ids.label)

    def on_leave(self,*args):
        if 'desktop' not in selected:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.5}, duration=.2)
            anim2=Animation(size_hint=(.2,.40), elevation=12, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.15}, font_size=15, duration=.2)
            anim1.start(self.ids.desktop)
            anim2.start(self)
            anim3.start(self.ids.label)

class Downloads(MDCard, HoverBehavior):
    def on_enter(self,*args):
        anim1=Animation(pos_hint={'center_x':.5, 'center_y':.65}, duration=.2)
        anim2=Animation(size_hint=(.22,.42), elevation=14, duration=.2)
        anim3=Animation(pos_hint={'center_x':.5, 'center_y':.3}, font_size=23,duration=.2)
        anim1.start(self.ids.downloads)
        anim2.start(self)
        anim3.start(self.ids.label)

    def on_leave(self,*args):
        if 'downloads' not in selected:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.5}, duration=.2)
            anim2=Animation(size_hint=(.2,.40), elevation=12, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.15}, font_size=15, duration=.2)
            anim1.start(self.ids.downloads)
            anim2.start(self)
            anim3.start(self.ids.label)

class Documents(MDCard, HoverBehavior):
    def on_enter(self,*args):
        anim1=Animation(pos_hint={'center_x':.5, 'center_y':.65}, duration=.2)
        anim2=Animation(size_hint=(.22,.42), elevation=14, duration=.2)
        anim3=Animation(pos_hint={'center_x':.5, 'center_y':.3}, font_size=23,duration=.2)
        anim1.start(self.ids.documents)
        anim2.start(self)
        anim3.start(self.ids.label)

    def on_leave(self,*args):
        if 'documents' not in selected:
            anim1=Animation(pos_hint={'center_x':.5, 'center_y':.5}, duration=.2)
            anim2=Animation(size_hint=(.2,.40), elevation=12, duration=.2)
            anim3=Animation(pos_hint={'center_x':.5, 'center_y':.15}, font_size=15, duration=.2)
            anim1.start(self.ids.documents)
            anim2.start(self)
            anim3.start(self.ids.label)



class MainScreen(Screen):
    pass


sm = ScreenManager()
expandable=True
selected=[]
desktop_selected=False
pictures_format=['.png', '.JPG', '.jpeg', '.gif', '.tif', '.bmp', '.webp', 'heif', '.svg','.jpg', '.ARW']
video_format=['.mp4','.mkv','.avi','.mpeg', '.mov', '.avchd', 'divx', '.flv', '.wmv', '.fla', '.mpg','.MTS']
documents_format=['.txt','.pdf','.docx','.docm','.dotx','.dotm','.docb','.doc','.xls','.xlt','.xlm','.xlsx','xlsm','xltx','xltm'
                    '.ppt','.pptx','.pot','.pps','.pptm','.potx','.potm','.ppsx','.ppsm','.sldx','.sldm']
zipped_format=['.zip','.7z','.rar','.iso','.tar','.s7z','.tar.gz','.tgz','.tar.Z','.tar.bz2','.tbz2','.tar.lz','.tlz','.tar.xz','.txz','.zipx']
audio_format=['.mp3','.wav','.mp3','.m4a','.aac','.aiff','.flac','.m4b','.ogg','.oga','.mogg','.raw','.wma','.webm']
installer_format=['.msi','.msp','.exe',]

class Mainapp(MDApp):


    def build(self):
        Builder.load_file("file_organizer.kv")
        sm.add_widget(MainScreen(name='MainScreen'))
        return sm

    def on_start(self):
        BuildMainScreen.load(self)


Mainapp().run()
