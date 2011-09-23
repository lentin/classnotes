import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    cmd = "pdftk */cover.pdf */model.pdf */karesel.pdf \
*/fundamental.pdf */euler.pdf */taylor.pdf \
*/logaritma.pdf */complexity.pdf */probsolve.pdf */id3.pdf \
*/turev.pdf */totaldiff.pdf */eigseg.pdf */rayleigh.pdf \
*/moment.pdf */dagilimlar.pdf */buyuk.pdf */cebisev.pdf \
*/ml-tr.pdf */naive.pdf */coal.pdf */simplex.pdf */qp.pdf \
*/svm.pdf */fem.pdf */fourier.pdf */heat.pdf */curvature.pdf \
*/level.pdf */varcalc.pdf */filter.pdf */phd.pdf \
output ~/Dropbox/Public/skfiles/app-math-tr.pdf "
    os.system(cmd)
    exit()