from plyer import notification  
  
notification_title = 'D3BUGGERS Greetings!'  
notification_message = 'Thank you for reading. Have a Good Day.'  
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    ) 