import os
import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TRegionDumperTest")

#import EventFilter.L1TXRawToDigi.util as util

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2016Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

process.load('L1Trigger.Configuration.SimL1Emulator_cff')
process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')
process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

process.load('L1Trigger.L1TCaloLayer1.simCaloStage2Layer1Digis_cfi')
process.simCaloStage2Layer1Digis.useECALLUT = cms.bool(True)
process.simCaloStage2Layer1Digis.useHCALLUT = cms.bool(True)
process.simCaloStage2Layer1Digis.useHFLUT = cms.bool(True)
process.simCaloStage2Layer1Digis.useLSB = cms.bool(True)
process.simCaloStage2Layer1Digis.verbose = cms.bool(True)
process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag("l1tCaloLayer1Digis")
process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag("l1tCaloLayer1Digis")

process.l1tRegionDumper = cms.EDAnalyzer(
    "L1TRegionDumper",
    UCTRegion = cms.untracked.InputTag('simCaloStage2Layer1Digis')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000000) )

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/FEF4A8AF-E449-E811-BF43-02163E017F01.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/04C0021C-E949-E811-B8E3-FA163ED6AFAF.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/8E862E39-E149-E811-AFA6-FA163E8561FE.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/04D04847-EF49-E811-B5C4-FA163E7C91C0.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/94437232-E149-E811-AC84-FA163E35307D.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/08244E72-E449-E811-AD12-FA163E5C078A.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/96103BDD-E449-E811-8770-FA163E82077C.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/089C26C8-FC49-E811-AF50-FA163E1CED1A.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/9C1A86A4-EF49-E811-AA1E-FA163E4543E4.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/0A56376D-E549-E811-A41C-FA163EBA050E.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/A84E952F-FC49-E811-89F6-FA163E188988.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/0EB50820-E549-E811-984A-FA163E306BAD.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/AEF1B31E-E149-E811-8272-FA163E059BE1.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/0EC67D18-E949-E811-95AF-FA163E6A65E5.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/B063B720-E549-E811-835F-FA163E4DDA9D.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/1064378F-F049-E811-B5EE-FA163E399AD5.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/B651F49C-E749-E811-9DC7-02163E017F3C.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/1820E187-E449-E811-A712-FA163EA40BD4.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/B8FE9D31-E149-E811-873E-FA163EE825DF.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/1AC52E00-F049-E811-8BF7-FA163E3E5663.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/BE526FC8-E749-E811-AC4E-FA163EA83FDB.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/26124CB2-EF49-E811-A1CA-FA163E9CA9FB.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/BEFC89B6-E449-E811-B377-FA163ED213E0.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/2C043B23-FC49-E811-8612-FA163E3E5663.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/C017B051-FC49-E811-A73F-FA163ED3E0A8.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/2C9C09DE-E449-E811-8FA1-FA163EC31C0F.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/C46347FF-E449-E811-9FCD-FA163E76D9E4.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/2CC7361E-FC49-E811-8FE3-FA163E60A5FD.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/C68250F8-E449-E811-A89F-FA163E09427C.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/34633AFC-E449-E811-8E64-02163E01A0CA.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/C6D524B2-EF49-E811-B886-FA163E7FF480.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/381071CD-EF49-E811-8D5C-02163E01A0CE.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/C8E680CA-EF49-E811-B597-FA163E5EFFAB.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/382E90E3-FB49-E811-ABA5-FA163E6A5AE1.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/CA7467F5-E449-E811-AE2F-FA163EF67044.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/4237D065-EF49-E811-9089-FA163E30D79B.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/E072182D-FC49-E811-A92D-FA163E6275D2.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/4C27A6E5-EF49-E811-B659-FA163EB46049.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/E4D83B09-FC49-E811-BD00-FA163EA0BB5F.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/4ED5009C-FC49-E811-83DC-FA163ECB69D1.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/E81075F1-E449-E811-BE6E-FA163E471DF7.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/509965A9-E749-E811-ACB7-FA163E4B6F1D.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/EA3B1B2A-FC49-E811-A6D9-FA163E7E37F5.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/5ADC514F-EF49-E811-9372-FA163E30BD36.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/EC3AD71E-E149-E811-946A-FA163E0B565D.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/5E9815AE-E449-E811-8DE2-FA163EA2C7DE.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/F0C925F9-FC49-E811-865A-02163E01487D.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/5ED89407-E549-E811-9309-FA163E8AF518.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/F0F9DD8C-EF49-E811-ADA7-FA163E37E91B.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/66E8045E-FC49-E811-9559-FA163E6BAD4B.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/F4052545-EF49-E811-8139-FA163E081C30.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/6A6EADA7-E449-E811-A03B-FA163E229782.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/F608FC44-F049-E811-8ECD-02163E0131C5.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/7014E491-EF49-E811-ACB2-FA163E0B9045.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/F62B19E2-EF49-E811-9C11-FA163ED05A75.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/74CA2138-FC49-E811-9432-FA163ED06402.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/FA2841CD-EF49-E811-8F0D-FA163EF3D946.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/7AE3B117-E149-E811-96C2-FA163ECF0DA2.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/FCED44EC-E749-E811-AD8E-FA163E3FB276.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/862C6A01-E549-E811-8959-FA163E82CF22.root',
        'file:/hdfs/store/data/Run2018A/ZeroBias/RAW/v1/000/315/267/00000/86506866-EF49-E811-B51A-FA163E2DB7A6.root'
    )
)

process.options = cms.untracked.PSet(
    
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string("l1TFullEvent.root"),
    outputCommands = cms.untracked.vstring('drop *')
)


#Output
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("l1TNtuple.root")
)

process.p = cms.Path(process.l1tCaloLayer1Digis*process.simCaloStage2Layer1Digis*process.l1tRegionDumper)

process.e = cms.EndPath(process.out)

process.schedule = cms.Schedule(process.p,process.e)

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

#dump_file = open('dump.py','w')
#dump_file.write(process.dumpPython())
