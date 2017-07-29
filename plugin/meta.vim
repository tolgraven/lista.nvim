if exists('g:loaded_meta')
  finish
endif
let g:loaded_meta = 1

function! s:start(qargs) abort
  return meta#start(a:qargs)
endfunction

function! s:resume(qargs) abort
  return meta#resume(a:qargs)
endfunction

command! -nargs=? Meta  call s:start(<q-args>)
command! MetaCursorWord call s:start(expand('<cword>'))

command! -nargs=? MetaResume  call s:resume(<q-args>)
command! MetaResumeCursorWord call s:resume(expand('<cword>'))