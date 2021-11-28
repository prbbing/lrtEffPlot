import os,sys
from ROOT import *

def ATLASLabel(x,y,shift,text="",color=1,size=0.04):
  l=TLatex()
  l.SetNDC()
  l.SetTextFont(72)
  l.SetTextColor(color)
  l.SetTextSize(size*(1.2))
  l.DrawLatex(x,y,"ATLAS")
  if (text!=""):
    p=TLatex()
    p.SetNDC();
    p.SetTextSize(size)
    p.SetTextFont(42)
    p.SetTextColor(color)
    p.DrawLatex(x+shift,y,text);

def myText(x,y,color=1,size=0.06,text=""):
  l=TLatex()
  l.SetTextSize(size);
  l.SetTextFont(42)
  l.SetNDC();
  l.SetTextColor(color);
  l.DrawLatex(x,y,text);

def drawAtlasLabel(label):
    myText(0.67,0.83,1,0.04,"#sqrt{s} = 13 TeV")
    ATLASLabel(0.15,0.83,0.16, "Simulation Internal")
    myText(0.15,0.75,1,0.04,label)

def formatEffHist(hist):
  hist.GetPaintedGraph().GetXaxis().SetLabelSize(0.03)
  hist.GetPaintedGraph().SetMinimum(0)
  hist.GetPaintedGraph().SetMinimum(2.0)
  hist.GetPaintedGraph().GetYaxis().SetTitle("Efficiency (#varepsilon)")
  hist.GetPaintedGraph().GetYaxis().SetLabelSize(0.03)
  hist.GetPaintedGraph().GetXaxis().SetTitleSize(0.03)
  hist.GetPaintedGraph().GetYaxis().SetTitleSize(0.03)
  hist.GetPaintedGraph().GetXaxis().SetTitleOffset(1.5)
  hist.GetPaintedGraph().GetYaxis().SetNdivisions(505)
  hist.GetPaintedGraph().GetXaxis().SetNdivisions(505)
  hist.GetPaintedGraph().GetYaxis().SetTitleOffset(1.5)
  hist.GetPaintedGraph().GetXaxis().SetTitle("Production Radius [mm]")
  hist.SetTitle("")
  hist.SetLineWidth(2)

inputFile_LRT = TFile("WH_lrt.root")
inputFile_STA = TFile("WH_sta.root")
inputFile_COM = TFile("WH_com.root")
outputFile = TFile("Eff.root","RECREATE")
outputFile.cd()

#eff_LRT = inputFile_LRT.Get("SquirrelPlots/LRT/Tracks/Efficiency/efficiency_vs_prodR").Clone()
#eff_STA = inputFile_STA.Get("SquirrelPlots/LRT/Tracks/Efficiency/efficiency_vs_prodR").Clone()
#eff_COM = inputFile_COM.Get("SquirrelPlots/LRT/Tracks/Efficiency/efficiency_vs_prodR").Clone()
eff_LRT = inputFile_LRT.Get("SquirrelPlots/LRT/Tracks/Efficiency/extended_efficiency_vs_absd0").Clone()
eff_STA = inputFile_STA.Get("SquirrelPlots/LRT/Tracks/Efficiency/extended_efficiency_vs_absd0").Clone()
eff_COM = inputFile_COM.Get("SquirrelPlots/LRT/Tracks/Efficiency/extended_efficiency_vs_absd0").Clone()

canvas = TCanvas("Eff","Eff", 600,600)
canvas.SetTickx(1)
canvas.SetTicky(1)

canvas.cd()

#eff_LRT.SetTitle(";Production Radius [mm];Technical Efficiency (#varepsilon_{tech})")
eff_LRT.SetTitle(";|d_{0}| [mm];Technical Efficiency (#varepsilon_{tech})")
eff_LRT.SetMarkerColor(6)
eff_LRT.SetLineColor(6)
eff_LRT.SetLineWidth(3)
eff_LRT.SetMarkerStyle(28)
eff_LRT.SetMarkerSize(1.2)
eff_LRT.Draw("AP")
eff_STA.SetMarkerColor(2)
eff_STA.SetLineColor(2)
eff_STA.SetMarkerStyle(27)
eff_STA.SetLineWidth(3)
eff_STA.SetMarkerSize(1.2)
eff_STA.Draw("P Same")
eff_COM.SetMarkerColor(1)
eff_COM.SetLineColor(1)
eff_COM.SetLineWidth(3)
eff_COM.SetMarkerSize(1.2)
eff_COM.SetMarkerStyle(20)
eff_COM.Draw("P Same")
gPad.Update()
formatEffHist(eff_LRT)
formatEffHist(eff_STA)
formatEffHist(eff_COM)
gPad.Update()
legend = TLegend(0.4, 0.55, 0.75, 0.7)
legend.SetBorderSize(0)
legend.SetTextFont(42)
legend.SetFillColor(0)
legend.SetTextSize(0.04)
legend.AddEntry(eff_COM,"Combined","p")
legend.AddEntry(eff_LRT,"Large Radius Tracking","p")
legend.AddEntry(eff_STA,"Standard Tracking","p")
legend.Draw("same")
drawAtlasLabel("WH (#rightarrowaa#rightarrowb#bar{b}b#bar{b}), c#tau_{a} = 100 mm")

canvas.Update()
canvas.Write()
outputFile.Close()
