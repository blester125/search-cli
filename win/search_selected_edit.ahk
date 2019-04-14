#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

get_selected_text() {
    tmp = %ClipboardAll% ;
    Clipboard := ;
    Sendinput, ^c ;
    ClipWait, 1 ;
    selection = %Clipboard% ;
    clipboard = %tmp% ;
    return selection
}

^+o::

x := get_selected_text() ;
run search_gui_highlighted %x%

return
