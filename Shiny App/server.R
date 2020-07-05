library(shiny)
library(shinydashboard)
library(jsonlite)
library(dqshiny)
library(httr)
library(readr)
library(tidyr)
library(stringr)
library(dplyr)
library(formattable)
URL = "http://127.0.0.1:5000/"
URL2 = "http://0.0.0.0:80/"
chrs = reactiveValues(list = list())
i = 1 
string = ""
function(input, output, session){
  ar
  my_list <- function(prefix){
    # simulate call to API, if user types 'a' the following is loaded into the drop down box
  #  character_vector = unlist(chrx)
  #  prefix = paste0(character_vector,collapse = "")
   # print(prefix)
    character_list = content(POST(URL,body = list(item = prefix),encode = "json"),as = "text")
    character2 = gsub('\\[\\"',"",character_list)
    character3 = gsub('\\"\\]',"",character2)
    character4 = gsub("\\\\t"," ",character3)
    character5 = gsub("[\\][n]?","",character4)
    character6 = gsub("\\[","",character5)
    character7 = gsub("\\]","",character6)
    splitted_auto = str_split(character7,'",',simplify = TRUE)
    for (i in (0:length(splitted_auto))){
      splitted_auto[i] = gsub('"',"",splitted_auto[i])
      splitted_auto[i] = gsub(',',"",splitted_auto[i])
    }
    return (as.list(splitted_auto))}
  
  observeEvent(input$pressedKey, {
    print (c("You have pressed ",input$pressedKeyId))
    if (!(input$pressedKeyId %in% c("Backspace", "Alt" , "Shift","Escape", "Tab" , "CapsLock","Control","Alt","Meta","Enter"))==TRUE){
      chrs$list  <<- append(chrs$list,input$pressedKeyId)}
    if(input$pressedKeyId=="Backspace" & length(chrs$list) != 0){
      chrs$list[length(chrs$list)] = NULL}
     character_vector = unlist(chrs$list)
     prefix = paste0(character_vector,collapse = "")
     print(prefix)
     text1 = my_list(prefix) 
     print(text1)
     updateSelectizeInput(session, 'auto', 
                         choices = text1,
                         selected = input$auto,
                         server = TRUE)
  })}

