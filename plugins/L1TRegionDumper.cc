// -*- C++ -*-
//
// Package:    L1Trigger/L1TRegionDumper
// Class:      L1TRegionDumper
//
/**\class L1TRegionDumper L1TRegionDumper.cc L1Trigger/L1TRegionDumper/plugins/L1TRegionDumper.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Sridhara Dasu
//         Created:  Tue, 11 Jan 2022 22:31:24 GMT
//
//

// system include files
#include <memory>
#include <vector>
#include <iostream>

// user include files

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

namespace l1tcalo {
  constexpr uint32_t RegionETMask{0x000003FF};
  constexpr uint32_t RegionEGVeto{0x00000400};
  constexpr uint32_t RegionTauVeto{0x00000800};
  constexpr uint32_t HitTowerBits{0x0000F000};
  constexpr uint32_t RegionNoBits{0x000F0000};
  constexpr uint32_t CardNoBits{0x00700000};
  constexpr uint32_t CrateNoBits{0x01800000};
  constexpr uint32_t NegEtaBit{0x80000000};
  constexpr uint32_t LocationBits{0xFFFFF000};
  constexpr uint32_t LocationShift{12};
  constexpr uint32_t RegionNoShift{16};
  constexpr uint32_t CardNoShift{20};
  constexpr uint32_t CrateNoShift{23};
}  // namespace l1tcalo


class L1TRegionDumper : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit L1TRegionDumper(const edm::ParameterSet&);
  ~L1TRegionDumper() {;};

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  // ----------member data ---------------------------
  
  edm::EDGetTokenT<std::vector <L1CaloRegion> > regionsToken_;  //used to select what tracks to read from configuration file
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
  edm::ESGetToken<SetupData, SetupRecord> setupToken_;
#endif

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
L1TRegionDumper::L1TRegionDumper(const edm::ParameterSet& iConfig)
  : regionsToken_(consumes<std::vector <L1CaloRegion> >(iConfig.getUntrackedParameter<edm::InputTag>("UCTRegion"))) {
  //now do what ever initialization is needed
}

//
// member functions
//

// ------------ method called for each event  ------------
void L1TRegionDumper::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  for (const auto& region : iEvent.get(regionsToken_)) {
    uint32_t ieta = region.id().ieta() - 4; // Subtract off the offset for HF
    uint32_t iphi = region.id().iphi();
    uint32_t regionSummary = region.raw();
    uint32_t et = (l1tcalo::RegionETMask & regionSummary);
    uint32_t location = ((regionSummary & l1tcalo::LocationBits) >> l1tcalo::LocationShift);
    bool eleBit = !((l1tcalo::RegionEGVeto & regionSummary) == l1tcalo::RegionEGVeto);
    bool tauBit = !((l1tcalo::RegionTauVeto & regionSummary) == l1tcalo::RegionTauVeto);
    std::cout       
      << ieta
      << "," << iphi
      << "," << et
      << "," << location
      << "," << eleBit 
      << "," << tauBit
      << std::endl;
  }

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void L1TRegionDumper::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(L1TRegionDumper);
