


CREATE TABLE `Nodes` (
	`NodeId` int NOT NULL AUTO_INCREMENT,
	`NodeName` varchar(255) NOT NULL,
	PRIMARY KEY (`NodeId`)
);

CREATE TABLE `NodeRelations` (
	`Node1` int NOT NULL,
	`Node2` int NOT NULL,
	`RelationID` int(255) NOT NULL,
	PRIMARY KEY (`Node1`,`Node2`)
);

CREATE TABLE `Relations` (
	`RelationID` int NOT NULL AUTO_INCREMENT,
	`Relation` varchar(255) NOT NULL,
	`Description` varchar(5000),
	PRIMARY KEY (`RelationID`)
);

ALTER TABLE `NodeRelations` ADD CONSTRAINT `NodeRelations_fk0` FOREIGN KEY (`Node1`) REFERENCES `Nodes`(`NodeId`);

ALTER TABLE `NodeRelations` ADD CONSTRAINT `NodeRelations_fk1` FOREIGN KEY (`Node2`) REFERENCES `Nodes`(`NodeId`);

ALTER TABLE `NodeRelations` ADD CONSTRAINT `NodeRelations_fk2` FOREIGN KEY (`RelationID`) REFERENCES `Relations`(`RelationID`);



insert into nodes(nodename) values ("GeoID"), ("fastsanger"), ("BAM"),("countMatrix"), ("Differential Analysis"), ("Gene Ontologies"), ("Heatmap"), ("SAM"),
         ("Drug name"), ("drug ID"),("drug pathway"), ("chemical compound name"), ("compound features"), ("DNA Sequence"),
         ("RNA Sequence"), ("Protein Sequence"), ("Sequence"),("sequence features"), ("FastQ"), ("Fasta"), ("Sequence ID"),
         ("Raw variants"), ("variants(indels and SNPs)");


insert into relations(relationid, relation) 
values (1,"Download fastsanger files using SRR Accesions from NCBI using the GeoID"),
(2,"Bowtie2"),(3,"featureCounts"),(4,"DESeq2"),(5,"geoseq"),(6,"heatmap2"),(7,"BWA"),(8,"Picard"),
		(9,"<name of some drug database to get drug ID>"),(10,"SMPDB"),(11,"FooDB"),(12,"HTSlib, and can be further compressed using gzip"),
        (13,"check compostion of sequence to determine the biomolecule(ATGC for DNA)"),
        (14,"check compostion of sequence to determine the biomolecule(AUGC for RNA)"),
        (15,"check compostion of sequence to determine the biomolecule(Amino Acids for Protein)"),
        (16,"common DNA features are: ATGC composition, mass, length, etc"),
        (17,"common RNA features are: AUGC composition, mass, length, etc"),
        (18,"common Protein features are: Amino Acid composition, mass, length, charge etc"),
        (19,"'sed -n <command> <input .fastq> > OUTFILE.fasta'"),
        (20,"seqtk subseq input.fasta name.list > output.fasta"),
        (21,"by mapping data to reference genome(may be done using BWA)"),
        (22,"variant caller like HaplotypeCaller or UnifiedCaller(for polyploid) of the GATK piepline"),
        (23,"By recalibrating the Raw variants using Variant Quality Scores (can be done by using GATK4 Pipeline.");

insert into noderelations(node1,node2,relationID) 
values (1,2,1),(2,3,2),(3,4,3),(4,5,4),(5,6,5),(6,7,6),
		(2,8,7),(8,3,8),(9,10,9),(10,11,10),(12,13,11),(3,19,12),
        (17,14,13),(17,15,14),(17,16,15),(14,18,16),(15,18,17),(16,18,18),
        (19,20,19),(21,20,20),(19,8,21),(3,22,22),(22,23,23);
        
