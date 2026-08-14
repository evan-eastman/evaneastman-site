# Refresh the Risk Theory Society page from the tracking workbook.
#
# The whole workflow after editing files/RTSPublicationTracking_*.xlsx:
#
#     .\tools\Update-RTS.ps1
#
# That reads the workbook, rewrites the data block inside rts.qmd, and renders
# the site. You never edit rts.qmd by hand and never touch JSON - the workbook
# is the only file you maintain.

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo

py -3 tools/build-rts-data.py
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Build failed. The page was not changed." -ForegroundColor Red
    exit 1
}

# Read the warnings above before moving on. The script reports rows it had to
# skip or could not parse; those are workbook problems, and they are silent on
# the rendered page.

quarto render rts.qmd
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Render failed." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Done. Preview it with:" -ForegroundColor Green
Write-Host "    quarto preview"
Write-Host ""
Write-Host "Then commit, and publish when you are ready:"
Write-Host "    git add -A; git commit -m 'Refresh the RTS record'"
Write-Host "    git push origin main"
Write-Host "    quarto publish gh-pages --no-prompt --no-browser"
