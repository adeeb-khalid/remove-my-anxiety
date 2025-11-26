from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.build_home_page()
  
  def build_home_page(self):
    """Build the home page welcome content using Material theme"""
    # Clear existing content
    self.content_panel.clear()
    
    # Main container with vertical spacing
    main_container = ColumnPanel(
      spacing_above='large',
      spacing_below='large'
    )
    
    # Welcome headline - using headline role from Material theme
    welcome_headline = Label(
      text="Welcome to Remove My Anxiety",
      role="headline",
      spacing_below='small',
      align='center'
    )
    main_container.add_component(welcome_headline)
    
    # Subtitle with secondary text styling
    subtitle = Label(
      text="Your safe space for daily support, calm guidance, and self-growth",
      role="subheading",
      spacing_below='large',
      align='center'
    )
    main_container.add_component(subtitle)
    
    # Main content card - using card role from Material theme
    content_card = ColumnPanel(
      role="card",
      spacing_above='medium',
      spacing_below='medium',
      spacing='medium'
    )
    
    # Welcome message paragraph
    welcome_para1 = Label(
      text="Remove My Anxiety is designed by mental health experts to help you manage anxiety step by step. We combine empathy with technology to provide you with the tools and support you need on your journey to wellness.",
      role="text",
      spacing_below='medium',
      spacing_above='medium'
    )
    content_card.add_component(welcome_para1)
    
    # Features section header
    features_label = Label(
      text="What You'll Find Here:",
      role="subheading",
      spacing_above='medium',
      spacing_below='small'
    )
    content_card.add_component(features_label)
    
    # Feature list
    features_text = Label(
      text="• Progress tracking to monitor your journey\n• Guided exercises for anxiety management\n• Gentle reminders that you're not alone\n• Evidence-based techniques and support",
      role="text",
      spacing_below='medium'
    )
    content_card.add_component(features_text)
    
    # Encouraging message
    encouragement = Label(
      text="Remember, taking the first step is already a victory. You're here, and that matters. Let's walk this path together, one step at a time.",
      role="text",
      spacing_above='medium',
      spacing_below='medium',
      italic=True
    )
    content_card.add_component(encouragement)
    
    # Add card to main container
    main_container.add_component(content_card)
    
    # Call-to-action section
    cta_container = ColumnPanel(
      spacing_above='large',
      spacing_below='large'
    )
    
    cta_label = Label(
      text="Ready to begin your journey?",
      role="subheading",
      spacing_below='medium',
      align='center'
    )
    cta_container.add_component(cta_label)
    
    main_container.add_component(cta_container)
    
    # Add main container to the existing content panel
    self.content_panel.add_component(main_container)
