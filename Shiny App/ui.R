library(shiny)
library(shinydashboard)


dashboardPage(
  dashboardHeader(),
  dashboardSidebar(),
  dashboardBody(
    
    tags$script('
                pressedKeyCount = 0;
                $(document).on("keyup", function (e) {
                Shiny.onInputChange("pressedKey", pressedKeyCount++);
                Shiny.onInputChange("pressedKeyId", e.key);
                });'),
    
    selectizeInput("auto",
                   "Clinically relevant Auto-complete Demo",
                   c(""),
                   selected="NONE",
                   options = list(plugins = list('restore_on_backspace'))),
    tags$style(type='text/css', ".selectize-dropdown-content {max-height: 1000px !important; }")
  )
)





 


